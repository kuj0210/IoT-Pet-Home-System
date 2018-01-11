# Pet House System
### Pet House System is a tool that allows you to manage through Messenger.

## **Features**
 - Usage through Messenger
 - Raspberry Pi with chat-bot based System
 - Using communication with flask server
 - Using 2 flask servers.(Main Server(in aws), PiServer(in raspberryPi))
 - You can check the status of your pet with PiCamera
 - You can manage meal and to give water to your pet(s).
 
## **Requirement**
 - Raspnerry Pi 3 module B (used in Pi Server)
 - 3 servo-motors(for meal,water,door) and PiCamera
 - Computer or Notebook(used to chat-bot API Server)
 - Smart Phone for using chat-bot(used in client)

## **Installation & Settings**

 **Setting**
 - Using 2 static ip address.
 - Main server is in AWS.(This server manage chat-bot API.)
 - PiServer is in RaspberryPi (This server manage RaspberryPi)
 - Using python 3.x version. Because Hangul generate error with uni-code/utf8.
 
 **Installation**
 **1) Server side**
 
  - Install MySQL.
  
  `sudo apt-get update
  sudo apt-get install mysql-server`
  
  - Install python3 modules; requests, flask, pymysql 
  
  `sudo pip3 install requests
   sudo pip3 install flask
   sudo pip3 install pymsql`
   
 **2) PiServer side**
  - Install GPIO modules.
  
  `sudo apt-get install python-dev
   sudo apt-get install python-rpi.gpio`
   
  - Install flask, requests modules.
  
  `sudo pip3 install flask
   sudo pip3 install requests`
