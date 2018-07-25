**Language**: [English](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/README.md/) [한글](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/README_KR.md/)

# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/pet_Image.jpg?raw=true" width="64">Pet House System
[![License: GPL v3](https://img.shields.io/badge/licence-GPL%20v3-yellow.svg)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/LICENSE)
<img src="https://img.shields.io/badge/python-%3E%3D3-brightgreen.svg">
<img src="https://img.shields.io/badge/release-v1.0.2-blue.svg">
[![Build Status](https://travis-ci.org/kuj0210/IoT-Pet-Home-System.svg?branch=master)](https://travis-ci.org/kuj0210/IoT-Pet-Home-System)
### Pet House System is a tool that enables you to manage pets through Messenger.



## Index
* [Introduction](#introduction)
* [Features](#features)
* [Requirement](#requirement)
* [Settings & Installation](#settings--installation)
  * [Settings](#settings)
  * [Installation](#installation)
* [Pet House Structure](#pet-house-structure)
* [Motor operation structure](#motor-operation-structure)
* [Client & Server Structure](#client--server-structure)
  * [Full server structure](#full-server-structure)
  * [Client & Main server structure](#client--main-server-structure)
  * [Main server & Pi-server structure](#main-server--pi-server-structure)
* [How to use](#how-to-use)
* [How to connect motor wires](#how-to-connect-motor-wires)
  * [Food Motor](#food-motor)
  * [Water Motor](#water-motor)
  * [Door Motor](#door-motor)
* [Notes](#notes)
* [Promotion(#promotion)
* [LICENSE](#license)

## Introduction

Pet House systems were built for people who would be absent from home and wouldn't be able to take care of their pets.
so it can help reduce pet worries because it is easy to manage pets when you are away on long trips or on sudden appointments.
It's very simple to use because it uses a messenger. If you are in an environment that has Internet access, you can use it anywhere.


## **Features**
 - Usage through Messenger
 - Raspberry Pi with chat-bot based System
 - Using communication with flask server
 - Using 2 flask servers.(Main Server(in aws), PiServer(in raspberryPi))
 - You can check the status of your pet with PiCamera
 - You can manage meal and to give water to your pet(s).


## **Requirement**
 ### H/W
 - Raspnerry Pi 3 module B (used in Pi Server)
 - 2 servo-motors(for meal,door) and PiCamera
 - Computer or Notebook(used to chat-bot API Server)
 - Smart Phone for using chat-bot(used in client)
 
 ### S/W
 - python 3.x
 - opencv-python 3.4.1.14
 - Required package: pymysql, requests, numpy, Flask, imutils

## **Settings & Installation**

### **Settings** 

 - Using 2 static ip address.
 - Main server is in AWS.(This server manage chat-bot API.)
 - PiServer is in RaspberryPi (This server manage RaspberryPi)
 - Using python 3.x version. Because Hangul generate error with uni-code/utf8.
 
### **Installation**
 
 **1) Server side**
  - Install MySQL.
  ```
  sudo apt-get update
  sudo apt-get install mysql-server
  ```
  
  - Install python3 modules; requests, flask, pymysql 
  ```
  sudo pip3 install requests
  sudo pip3 install flask
  sudo pip3 install pymsql
  ```
   
 **2) PiServer side**
  - Install GPIO modules.
  ```
  sudo apt-get install python-dev
  sudo apt-get install python-rpi.gpio
  ```
   
  - Install flask, requests modules.
  ```
  sudo pip3 install flask
  sudo pip3 install requests
  ```

## **Pet House Structure**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Pet_House_Structure.png?raw=true)

Three motors are operated by messenger, and manage feeds, water and door.<br>
And you can see the pet directly through the Pi Camera.


## **Motor operation structure** 

| **Door(open)** | **Door(close)** |
| :----: | :----: |
|![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_open.png?raw=true) <br> Open the door by pulling the thread by the rotation of the motor | ![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_close.png?raw=true) <br> When the motor stops, the door is closed by the resilience of the weight. |
| **Food** | - |
| ![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_food.png?raw=true) <br> Rotate and restore the motor for a short time, and feed the prey by opening and closing the entrance  | - |




## **Client & Server Structure**

### **Full server structure**

![](https://github.com/kuj0210/opensourceproject/blob/master/.README/Client&Server_Structure.png?raw=true)


- Client: The client represents a user using messanger application.
- Server(Main Server): This server is main of full structure. It manage chatbot and commands for controlling PiServer.
- PiServer(RaspberryPi): This server manage to control motors, camera and push thread.


### **Client & Main server structure**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Structure_client&mainserver.png?raw=true)


 Client will order various commands. (regist user, control to pet-home etc) And the main-server get this commands. Before main-server get this commands, messages go to API server and API server give the data to main-server.(data:json type) After main-server get this type's data, it'll parse this data and make operation list for ordering to PiServer. The main-server send operation list to PiServer and make reply-message for sending to user.<br>
 But if a user don't register to server or don't registered in PiServer's userlist, this user can't use this chatbot. Main-server use database for managing user-data and registed Pi-servers. Below inform main-server and pi-server structure.


### **Main server & Pi-server structure**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Structure_mainserver&piserver.png?raw=true)


This structure is main-server and pi-server(in RaspberryPi using flask framework) structure. Before the Pi-server open flask server, this server send user and this device's information(registed userlist and PiKey) to main server. If this communication come into existence(communication success), the pi-server is ready to get data from main-server. The main server send operation list to pi-server by user's order. Pi-Server parse these, order to each of motor or pi-camera for implement of user's commands. And then, after implement of user's commands, pi-server send result-data to main-server. The main-server parse this data, make the appropriate reply and finally send json type data to API server. (This json data will become reply message; it is shown reply message to user.)


## **How to use**


**1) Add Official account of Messanger(IoT Pet House System)**

 - kakao-talk platform: @guineapighome (IoT 펫홈 관리 시스템)<br> 
 - naver-talktalk platform: IoT 펫홈 시스템

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_first.PNG?raw=true)


**2) Enter chat in the format “[등록]/e-mail/Product-Key”**

 Check your device's product-key, and regist your email and product-key to chatbot-server.<br>
 If you don't regist, chatbot-server don't support your command. 
 
![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_regist.PNG?raw=true)


**3) Enter chats that associated with food, water and door opening.**

If you're a registed user, you can do chatting with IoT-pet-home-system!<br>
Order to set feed, water or open pet-home door at the IoT-pet-home-system chatbot.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_operation.PNG?raw=true)


**4) If you don't know how to use or need to remind your account, please enter the command below.**

- "[사용법]" : This command will inform how to use this chatbot.<br>
- "[정보]" : This command will inform your account that you registed at this chatbot-server.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_etc.PNG?raw=true)


**5) If you forget to feed or set water to your pet, chatbot's push service support you!**

- If you don't set feed or water to your pet, push alarm inform to you once an hour.
- But this service only support at naver-talk-talk platform. (Kakao-talk platform don't support it.)

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_push.PNG?raw=true)
     



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



 ## **Notes**
 
 - Installation method of Rasbian<br>
   https://www.raspberrypi.org/documentation/installation/installing-images/

 - [DB Query description (MySQL)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/DB_Query_description.md)
 
 - Apply from public IP to HTTPS
   1. [AWS EC2 setting guide](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md)
   2. [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)
   3. [How to use SSL Certificates and apply HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS.md)

 ## **Promotion**
 
  - In issue#36 :: Reference PPT and video(참고용 PPT 및 동영상)<br>
   https://github.com/kuj0210/IoT-Pet-Home-System/issues/36
 
 ## **LICENSE**
 
 IoT-Pet-Home-System is licensed under [the GNU GENERAL PUBLIC LICENSE v3](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/LICENSE).
 
 ```
 Copyright (C) 2017-present, kuj0210, KeonHeeLee, seok8418

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
