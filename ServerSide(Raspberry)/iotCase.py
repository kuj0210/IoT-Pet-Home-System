import time
import grovepi
import math
import threading
from grovepi import *
import socket
import picamera
import os
import sys

################## For Sensor & Sensor Data ##################

# Connections
temperature_sensor = 7  # port D2
ultrasonic_ranger = 4
buzzer_pin = 3		#Port for buzzer

pinMode(buzzer_pin,"OUTPUT")	# Assign mode for buzzer as output
digitalWrite(buzzer_pin,0)

global t
global h
[t,h]=[0,0]  # check temperature & humidity

################# Server side socket ############################

host = ''
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

serversocket.bind((host, port))
serversocket.listen(1)

################# other init values ############################

mode = 'off' # off : not connected / on : connecting
initDistant = 0
request = ''
path = ''


####################### Thread1  ###############################

def DetectingThread(default):
# for counting second
    counter = 0

    while True:
        global mode
        if mode == 'on':
            distant = ultrasonicRead(ultrasonic_ranger)
            global initDistant
            initDistant = distant
            while mode == 'on':
                distant = ultrasonicRead(ultrasonic_ranger)
                global t
                global h
                [t,h] = grovepi.dht(temperature_sensor,0)
                print (counter,')',distant,'cm')
                print (t,h)

                try:
                    if t >= 80:
                        str = "Warning! Your case is Overhit!! (Temp: %d, Humidity: %d)" %(t,h)
                        os.system("nodejs fcm-pushserver.js");
                        while True:
                            [t,h] = grovepi.dht(temperature_sensor,0)
                            digitalWrite(buzzer_pin,1)
                            if t < 30:
                                digitalWrite(buzzer_pin,0)
                                break
                            time.sleep(1)
                    if counter != 5 :
                        if distant > initDistant + 5: # open case
                            counter += 1                 

                        else :  # close case
                            counter = 0
                            digitalWrite(buzzer_pin,0) 

                    else : #counter == 5
                        now = time.localtime()
                        out_str ="Check your case.(%04d-%02d-%02d %02d:%02d:%02d)" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                        print (out_str)
                        digitalWrite(buzzer_pin,1)
                        os.system("nodejs fcm-pushserver2.js");
                        with picamera.PiCamera() as camera:
                            camera.start_preview()
                            time.sleep(1)             

                            global path
                            path = '/home/pi/Pictures/Record %04d-%02d-%02d %02d:%02d:%02d.png' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                            camera.capture(path)
                            camera.stop_preview()

                        counter = 0

                except IOError:
                    print("Error")
                except KeyboardInterrupt:
                    exit()

                time.sleep(1)
        elif mode == 'off':
            print "Don't exist requestion."
            time.sleep(1)      

if __name__ == "__main__":
    d = threading.Thread(target=DetectingThread, args=('hello',))

    d.daemon = True
    d.start()

    while True:
        conn, addr = serversocket.accept()
        print('Connected by', addr)
        request = conn.recv(1024)
        request.decode('utf-8')

        if not request: break

        if request == 'on':
            mode = request
            print('Sensor On')
            conn.sendall(request)
        elif request == 'off':
            mode = request
            print('Sensor Off')
            digitalWrite(buzzer_pin,0)
            conn.sendall(request)
        elif request == 'get':
            print(path)
            print('Sending... :' + path)
            f = open(path,'rb')
            lread = f.read(10240)
            while (lread) :
                conn.send(lread)
                lread = f.read(10240)
            f.close()
            print('Sending file complete! :'+path)
        elif request == 'set':
            print('Preparing sensor data...')
            th = str(t)+','+str(h)
            sendMsg = th.encode('utf-8')
            print(sendMsg)
            conn.sendall(sendMsg)
            print('Sent sensor data!' + sendMsg)

        else :
            print "Not supporting request..."
                    
        conn.close()

    serversocket.close()
    print "Server exit..."
    ##d = DetectingThread()
    ##d.start()