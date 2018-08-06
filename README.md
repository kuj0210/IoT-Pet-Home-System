

# <img src="./docs/repo/pet_Image.jpg?raw=true" width="64">Pet House System
[![License: GPL v3](https://img.shields.io/badge/licence-GPL%20v3-yellow.svg)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/LICENSE)
<img src="https://img.shields.io/badge/python-%3E%3D3-brightgreen.svg">
<img src="https://img.shields.io/badge/release-v1.0.2-blue.svg">
[![CONTRIBUTORS](https://img.shields.io/badge/contributors-4-green.svg?style=flat-square)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/CONTRIBUTERS.md)
[![HitCount](http://hits.dwyl.io/kuj0210/IoT-Pet-Home-System.svg)](http://hits.dwyl.io/kuj0210/IoT-Pet-Home-System)
[![Build Status](https://travis-ci.org/kuj0210/IoT-Pet-Home-System.svg?branch=master)](https://travis-ci.org/kuj0210/IoT-Pet-Home-System)
<br><h4>IoT-Pet-Home-System is a system that can communicate through pet-homes and chatting-bot. 

# How To Get Source Code ?
- Go To **[IoT-Pet-Home-System-Project](https://github.com/IoT-Pet-Home-System)**

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
 - Raspberry Pi 3 module-B (used in Pet-home-System)
 - 2 servo-motors(for feed, door) and PiCamera
 - Server with public IP(used to chat-bot API Server) and HTTPS.
 - Smart-Phone or web for using chat-bot(used in client)
 
 ### S/W
 - python 3.x version
 - Open-jdk and g++
 - opencv-python 3.4.1.14
 - Raspbian OS(for pethome)
 - Required package: requests, Flask, pymysql, numpy, imutils, konlpy
 
## Others
 - Must regist to **Naver-talktalk Partner**.

## **Pet House Structure**

![](./docs/image/pethome/Pet_House_Structure.png?raw=true)

Three motors are operated by messenger, and manage feeds and door.<br>
And you can see the pet directly through the Pi Camera.


## **Motor operation structure** 

| **Door(open)** | **Door(close)** | **Food** |
|----------------|-----------------|----------|
|<img src="./docs/image/motor/motor_open.png?raw=true" width="235">|<img src="./docs/image/motor/motor_close.png?raw=true" width="235">| <img src="./docs/image/motor/motor_food.png?raw=true" width="235">|
|Open the door by pulling the thread by the rotation of the motor| When the motor stops, the door is closed by the resilience of the weight.| Rotate and restore the motor for a short time, and feed the prey by opening and closing the entrance|


## **Client & Server Structure**

### **Full server structure**

![](./docs/image/structure/Full_server_structure.png?raw=true)

- **User <-> Chatting-Bot**

1. Users who use Naver-TalkTalk send messages to chatbots using Naver-talkTalk web application.
2. Naver-TalkTalk API Server sends messages from users as JSON type to a chatting-bot server.
3. The Chatting-Bot Server compares and analyzes the data stored in the DB with this data. Process the data and send the appropriate response to the user.
4.The Naver-TalkTalk API server processes the message to a user, which is readable by the user, and then presents the result to the user.

- **Chatting-Bot <-> Pet-Home**

1. Pet-Home constantly asks the chatting-bot server if there are any requests from the user.
2. The chatting-Bot server checks the DB when a request is received from Pet-Home and sends it to Pet Home if requested by the user.
3. Pet-Home, which is requested, performs this tasks.


### **Client & Main server structure**

![](./docs/image/structure/Client&main_server_structure.png?raw=true)

1. Users send requests to Pet Home through the Navertalk web application. Naver-TalkTalk API server then recognizes this and sends data to chatting-bot server.
2. Chatting-Bot Server obtain data(request) and a user-key from Naver-TalkTalk. Save the user-key and data(request).
3. After that, look at the user-key that Pet-Home registered for and see what requests it had. Then take the request and do the corresponding work.
4. When Pet-Home has finished all the requests of its registered user, it sends a push notification to the user.


## **How to use**

**1) Add Official account of Messanger(IoT Pet House System)**

 - **naver-talktalk platform**: IoT 펫홈 시스템

![](./docs/how_to_use/image/How_to_use.png?raw=true)


**2) Enter chat in the format "등록"**

 - When you enter this command, it sends the registration url.
 
![](./docs/how_to_use/image/get_regist_url.png?raw=true)


**3) Click url and fill in the User-Registration form.**

 - Check your ```pet-home's serial-key``` and enter the ```serial-key```, ```E-mail adress```, ```pet-home nickname```
 and ```the number of pets``` into below form. And then press the button;```submit``` below to regist.

![](./docs/how_to_use/image/regist_form.png?raw=true)


**4) Enter chats that associated with food, door opening, Taking pictures.**

 - If you're a registed user, you can do chatting with IoT-pet-home-system!<br>
Order to ```set feed```, ```open pet-home's door``` at the IoT-pet-home-system chatbot.

![](./docs/how_to_use/image/request.png?raw=true)

<br>

- Ask Chatbot to ```take picture```.

![](./docs/how_to_use/image/capture_request.png?raw=true)


**5) If you don't know how to use, please enter the command below.**

 - "[사용법]" : This command will inform how to use this chatbot.<br>

![](./docs/before/image/naver_talktalk/chatbot_etc.PNG?raw=true)

**6) If you forget to feed your pet, chatbot's push service support you!**

 - If you don't set feed your pet, push alarm inform to you once an hour.

![](./docs/how_to_use/image/chatbot_push.png?raw=true)
    
    
**7) If you want to stop a talktalk-friend, you can stop anytime.**

- All information you entered at the time of registration will be deleted and the following message will be sent to you.

![](./docs/how_to_use/image/cancle_friend.png?raw=true)   ![](./docs/how_to_use/image/cancle_message.png?raw=true)



 ## **Notes**
 
 ### Installation of the Systems.
 
  **1) Server side**
  - Install ```MySQL``` and ```compiler```s.
  ```bash
  $ sudo apt-get update
  $ sudo apt-get install mysql-server
  $ sudo apt-get install g++ openjdk-7-jdk
  ```
  
  - Install python3 packages; ```requests```, ```flask```, ```pymysql``` , ```KoNLPy```
  ```bash
  $ pip3 install requests
  $ pip3 install flask
  $ pip3 install pymsql
  $ pip3 install konlpy
  ```
  
  - Clone repository and Setting configurations
  ```bash
  $ cd src
  $ sudo chmod +0777 setting.sh
  $ ./setting.sh
  ```
   
 **2) Pet-Home side**
  - Install GPIO modules.
  ```bash
  $ sudo apt-get install python-dev
  $ sudo apt-get install python-rpi.gpio
  ```
 
  - Install python3 packages; ```requests```, ```numpy```, ```imutils```
  ```bash
  $ pip3 install requests
  $ pip3 install numpy
  $ pip3 install imutils
  ```
  - Install openCV-python
  ```bash
  $ pip3 install opencv-python
  ```

 ### README by version
 
 - [README - 1.0.2 version](./docs/before/README(1.0.0).md)
 - [README(KR) - 1.0.2 version](./docs/before/README_KR(1.0.0).md)
 
 ## **Promotion**
 
  - In issue#36 :: Reference PPT and video(참고용 PPT 및 동영상)<br>
   https://github.com/kuj0210/IoT-Pet-Home-System/issues/36
 
 ## **LICENSE**
 
### Main-server (ChattingBot)

IoT-Pet-Home-System's main-server is licensed under [the GNU GENERAL PUBLIC LICENSE v3](https://www.gnu.org/licenses/gpl-3.0.html).
 
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
