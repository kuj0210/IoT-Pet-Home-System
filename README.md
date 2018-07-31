- **Language**: [English](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/README.md/) <br>
- Go To **[IoT-Pet-Home-Team](https://github.com/IoT-Pet-Home-System)**

# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/pet_Image.jpg?raw=true" width="64">Pet House System
[![License: GPL v3](https://img.shields.io/badge/licence-GPL%20v3-yellow.svg)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/LICENSE)
<img src="https://img.shields.io/badge/python-%3E%3D3-brightgreen.svg">
<img src="https://img.shields.io/badge/release-v1.0.2-blue.svg">
[![CONTRIBUTORS](https://img.shields.io/badge/contributors-4-green.svg?style=flat-square)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/CONTRIBUTERS.md)
[![HitCount](http://hits.dwyl.io/kuj0210/IoT-Pet-Home-System.svg)](http://hits.dwyl.io/kuj0210/IoT-Pet-Home-System)
[![Build Status](https://travis-ci.org/kuj0210/IoT-Pet-Home-System.svg?branch=master)](https://travis-ci.org/kuj0210/IoT-Pet-Home-System)
### Pet House System is a tool that enables you to manage pets through Messenger.



## Index
* [Introduction](#introduction)
* [Features](#features)
* [Requirement](#requirement)
* [Pet House Structure](#pet-house-structure)
* [Motor operation structure](#motor-operation-structure)
* [Client & Server Structure](#client--server-structure)
  * [Full server structure](#full-server-structure)
  * [Client & Main server structure](#client--main-server-structure)
* [How to use](#how-to-use)
* [Notes](#notes)
* [Promotion](#promotion)
* [LICENSE](#license)

## Introduction

Pet House systems were built for people who would be absent from home and wouldn't be able to take care of their pets.
so it can help reduce pet worries because it is easy to manage pets when you are away on long trips or on sudden appointments.
It's very simple to use because it uses a messenger. If you are in an environment that has Internet access, you can use it anywhere.


## **Features**
 - Usage through Messenger.
 - Raspberry Pi with chat-bot based System.
 - Using communication with chat-bot server(based on flask).
 - You can check the status of your pet with PiCamera.
 - You can manage meal for your pet(s).


## **Requirement**
 ### H/W
 - Raspberry Pi 3 module B (used in Pi Server)
 - 2 servo-motors(for meal,door) and PiCamera
 - Server with public IP(used to chat-bot API Server) and HTTPS.
 - Smart-Phone or web for using chat-bot(used in client)
 
 ### S/W
 - python 3.x version
 - Open-jdk and g++
 - opencv-python 3.4.1.14
 - Raspbian OS(for pethome)
 - Required package: requests, Flask, pymysql, numpy, imutils


## **Pet House Structure**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Pet_House_Structure.png?raw=true)

Three motors are operated by messenger, and manage feeds and door.<br>
And you can see the pet directly through the Pi Camera.


## **Motor operation structure** 

| **Door(open)** | **Door(close)** |
| :----: | :----: |
|![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_open.png?raw=true) <br> Open the door by pulling the thread by the rotation of the motor | ![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_close.png?raw=true) <br> When the motor stops, the door is closed by the resilience of the weight. |
| **Food** | - |
| ![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/motor_food.png?raw=true) <br> Rotate and restore the motor for a short time, and feed the prey by opening and closing the entrance  | - |




## **Client & Server Structure**

### **Full server structure**

![](https://github.com/kuj0210/opensourceproject/blob/master/.README/Full_server_structure.png?raw=true)


- User: User represents a user using messanger application.
- Chatting Server(Main Server): This server is main of full structure. It manage chatbot and commands for controlling PiServer.
- PiServer(RaspberryPi): This server manage to control motors, camera and push thread.

 
 The right part represent the main-server and pi-server(in RaspberryPi using flask framework) structure. Before the Pi-server open flask server, this server send user and this device's information(registed userlist and PiKey) to main server. If this communication come into existence(communication success), the pi-server is ready to get data from main-server. The main server send operation list to pi-server by user's order. Pi-Server parse these, order to each of motor or pi-camera for implement of user's commands. And then, after implement of user's commands, pi-server send result-data to main-server. The main-server parse this data, make the appropriate reply and finally send json type data to API server. (This json data will become reply message; it is shown reply message to user.)


### **Client & Main server structure**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Client&main_server_structure.png?raw=true)


 Client will order various commands. (regist user, control to pet-home etc) And the main-server get this commands. Before main-server get this commands, messages go to API server and API server give the data to main-server.(data:json type) After main-server get this type's data, it'll parse this data and make operation list for ordering to PiServer. The main-server send operation list to PiServer and make reply-message for sending to user.<br>
 But if a user don't register to server or don't registered in PiServer's userlist, this user can't use this chatbot. Main-server use database for managing user-data and registed Pi-servers. Below inform main-server and pi-server structure.


## **How to use**


**1) Add Official account of Messanger(IoT Pet House System)**

 - kakao-talk platform: @guineapighome (IoT 펫홈 관리 시스템)<br> 
 - naver-talktalk platform: IoT 펫홈 시스템

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/How_to_use.png?raw=true)


**2) Enter chat in the format “등록”**

 When you enter this command, it sends the registration url
 
![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/get_regist_url.png?raw=true)

**3) Click url and fill in the text box.

Check your device's product-key and enter the product key, E-mail adress, pet home nickname, and then the number of pets.<br>
Then press the button below to register.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/get_regist_url.png?raw=true)


**4) Enter chats that associated with food, door opening, Taking pictures.**

If you're a registed user, you can do chatting with IoT-pet-home-system!<br>
Order to set feed, open pet-home door at the IoT-pet-home-system chatbot.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/request.png?raw=true)

Ask Chatbot to take pictures.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/capture_request.png?raw=true)

**5) Enter chats that associated with camera.**

If you're a registed user, you can do chatting with IoT-pet-home-system!<br>
Order to set feed, open pet-home door at the IoT-pet-home-system chatbot.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/request.png?raw=true)

**6) If you don't know how to use or need to remind your account, please enter the command below.**

- "[사용법]" : This command will inform how to use this chatbot.<br>
- "[정보]" : This command will inform your account that you registed at this chatbot-server.

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/chatbot_etc.PNG?raw=true)


**7) If you forget to feed your pet, chatbot's push service support you!**

- If you don't set feed your pet, push alarm inform to you once an hour.
- But this service only support at naver-talk-talk platform. (Kakao-talk platform don't support it.)

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/chatbot_push.png?raw=true)
    
    
**8) If you forget to feed your pet, chatbot's push service support you!**

- If you don't set feed your pet, push alarm inform to you once an hour.
- But this service only support at naver-talk-talk platform. (Kakao-talk platform don't support it.)

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/How_to_use/chatbot_push.png?raw=true)




 ## **Notes**

  [DB Query description (MySQL)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/DB_Query_description.md)
 
 
 ### Installation of the modules
 
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
  - Install flask, requests, numpy, imutils modules.
  ```
  sudo pip3 install flask
  sudo pip3 install requests
  sudo pip3 install numpy
  sudo pip3 install imutils
  ```
  - Install openCV-python
  ```
  sudo pip3 install opencv-python
  ```

 ### README by version
 
 [README - 1.0.0 version](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/README(1.0.0).md)
 
 [README(KR) - 1.0.0 version](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/README_KR(1.0.0).md)
 
 ## **Promotion**
 
  - In issue#36 :: Reference PPT and video(참고용 PPT 및 동영상)<br>
   https://github.com/kuj0210/IoT-Pet-Home-System/issues/36
 
 ## **LICENSE**
 
### Main-server (ChattingBot)

IoT-Pet-Home-System's main-server is licensed under [the GNU GENERAL PUBLIC LICENSE v3](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/ChattingBot/LICENSE).
 
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

### PetHome

IoT-Pet-Home-System's pet-home is licensed under [the 3-clause BSD LICENSE](https://opencv.org/license.html).
```
By downloading, copying, installing or using the software you agree to this license. 
If you do not agree to this license, do not download, install, copy or use the software.

License Agreement
For Open Source Computer Vision Library
(3-clause BSD License)

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer. Redistributions in binary form must reproduce 
the above copyright notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution. Neither the names 
of the copyright holders nor the names of the contributors may be used to endorse or promote 
products derived from this software without specific prior written permission. This software 
is provided by the copyright holders and contributors “as is” and any express or implied 
warranties, including, but not limited to, the implied warranties of merchantability and 
fitness for a particular purpose are disclaimed. In no event shall copyright holders or 
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential 
damages (including, but not limited to, procurement of substitute goods or services; loss of use, 
data, or profits; or business interruption) however caused and on any theory of liability, whether 
in contract, strict liability, or tort (includingnegligence or otherwise) arising in any way out 
of the use of this software, even if advised of the possibility of such damage.
```
