# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/RaspberryPi_Logo.jpg?raw=true" width="64">Raspberry Pi Setting

## **Install Rasbian**

 - Installation method of Rasbian<br>
   https://www.raspberrypi.org/documentation/installation/installing-images/

## **How to use Raspberry Pi Camera**

1. Install the Raspberry Pi Camera module by inserting the cable into the Raspberry Pi. 
The cable slots into the connector situated between the Ethernet and HDMI ports, 
with the silver connectors facing the HDMI port.

2. Boot up your Raspberry Pi.

3. From the prompt, run "sudo raspi-config".
```
sudo raspi-config
```

4. If the "camera" option is not listed, you will need to run a few commands to update your Raspberry Pi. 
Run "sudo apt-get update" and "sudo apt-get upgrade"
```
sudo apt-get update
sudo apt-get upgrade
```

5. Run "sudo raspi-config" again - you should now see the "camera" option.
![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Enable_Camera.png?raw=true)

6. Navigate to the "camera" option, and enable it. Select “Finish” and reboot your Raspberry Pi.


   
## **How to connect motor wires**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/raspberry-pi-pinout.png?raw=true)


### Food Motor

- Orange wired: connects to pin 35
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

### Door Motor

- Orange wired: connects to pin 12
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)



