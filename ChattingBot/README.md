# IoT-Pet-Home-System : ChattingBot Server

 This server is main part of this system. For example, it not only recieve and send payload related to Naver-talktalk 
messenger API from client, but also analyze nature language(Korean), receive device's requests and send the device's works.


## Requirement

### 1. Modules

- **openjdk-7-jdk** : KoNLPy package request JVM.
- **g++** : KoNLPy package request this.
- **Python3** : It is required to solve utf-8 issues and packages.
- **MySQL** : This system use this database.

### 2. Environment

- **Public IP** : This server must have public IP(to handle API server & support cloud).
- **HTTPS** : This server only support on HTTPS protocol environment.

## Dependency

- flask
- KoNLPy
- requests
- PyMySQL

## Installation

### 1. Requirement(modules)

```bash
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ sudo apt-get install g++ openjdk-7-jdk
$ sudo apt-get install python3-dev
$ sudo apt-get install git # If you don't install it...
```

### 2. Dependency

- Case::**Python3**
```bash
$ pip3 install flask
$ pip3 install konlpy
$ pip3 install requests
$ pip3 install pymysql
```

### 3. Clone this repository

```bash
$ git clone https://github.com/kuj0210/IoT-Pet-Home-System
```

## Usage

```bash
$ cd ChattingBot  #In this repository's root directory
$ sudo python3 Server.py
```

## Introduce Internal Modules

- **api** : To handle NaverTalkTalk API payload.
- **auth** : Management authentication related to sign up and issue temp ID for registration step. 
- **db** : To handle database and data related to this system.
- **memo** : To handle cache related a images from devices.
- **nl** : To analyze Nature Language and pick main keyword for operating each devices or replying to user.
- **reply** : Management of reply messages to send user.
- **static & template** : To manage html template, script source codes(Javascript), css and favicon. 
- **test** : You can test this system, to use this module.
- **Server.py** : Main part of this system. It recieve and send payloads with HTTPS to client.

## Membership Management and DB Explanation

 This system's database is based on 1 database and 5 tables.

### SystemData (database)

This database include the 5 tables. Below tables is them.

- naverUser

```sql
user_key varchar(50) primary key,
serial varchar(50) primary key,
Email varchar(100),
petName varchar(50)
```

 This table is used to manage user data related to regist this system. UserKey and Serial is used to search another keys or tuples.
 
 - TempID
 
 ```sql
user_key varchar(50) primary key,
ID varchar(50) primary key
 ```
 
  This table is used to temporarily manage user_key. But user related on this table isn't this system's user, accordingly this user's 
  information isn't registed in naverUser table. If you regist in this system, this table's tuple will be deleted.
  
  - OldImageList
  
  ```sql
addr varchar(100) primary key,
serial VARCHAR(50)
  ```
  
 This table is used to temporarily manage cache related image what is sent to devices. Therefore, this system write device's serial
 related on sending image and cache's path(relate path).
 
 - homeSystem
 
 ```sql
serial varchar(50) primary key,
petCount int default 1
 ```

 This table is used to manage device's information. Specially serial is very important to use or search other data.
 
 - request
 
 ```sql
serial varchar(50),
requestor varchar(50),
request varchar(50),
FOREIGN KEY (serial) REFERENCES homeSystem (serial)
 ```
 
 This table is used to manage device's request list. If a user(registed user) request any operation(s), this server will save it.
After a device request to its works in database, server will send this list and delete this tuple. This tuple is device's works.


## Note

 - Apply from public IP to HTTPS
   1. [AWS EC2 setting guide](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md)
   2. [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)
   3. [How to use SSL Certificates and apply HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS.md)
