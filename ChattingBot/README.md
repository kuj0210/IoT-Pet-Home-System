# IoT-Pet-Home-System : ChattingBot Server

 This server is main part of this system. For example, it not only recieve and send payload related to Naver-talktalk 
messenger API from client, but also analyze nature language(Korean), receive pet-home's requests and send the pet-home's works.


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

- **api** : This module handle NaverTalkTalk(Web application messenger used by this system) API payload.
- **auth** : This module manage authentication related to sign up and issue temporary ID for registration step. 
- **db** : This module handle database and data related to this system.
- **memo** : This module memorize cache related a images recieving from pet-homes and if this cache isn't unecessary, this module delete it.
- **nl** : This module analyze Nature Language(Korean) and pick main keyword for operating each pet-homes or replying to user.
- **reply** : This module manage of reply messages to send user.
- **static & template** : This module manage html template, script source codes(Javascript), css and favicon. Specially, this system refer about user registration form.
- **test** : You can test this system, to use this module.
- **Server.py** : Main part of this system. It recieve and send payloads with HTTPS to client.

## DB Explanation and Membership Management

### DB Explanation

This system include 1 database and 5 tables. Below tables is them. <br/>
Main database is ```SystemData``` and this database include below 5 tables.

- **naverUser**

```sql
user_key varchar(50) primary key,
serial varchar(50) primary key,
Email varchar(100),
petName varchar(50)
```

 This table is used to manage user data related to regist this system. UserKey and Serial is used to search another keys or tuples.
 
 - **TempID**
 
 ```sql
user_key varchar(50) primary key,
ID varchar(50) primary key
 ```
 
  This table is used to temporarily manage user_key. But user related on this table isn't this system's user, accordingly this user's 
  information isn't registed in naverUser table. If you regist in this system, this table's tuple will be deleted.
  
  - **OldImageList**
  
  ```sql
addr varchar(100) primary key,
serial VARCHAR(50)
  ```
  
 This table is used to temporarily manage cache related image what is sent to pet-homes. Therefore, this system write pet-home's serial
 related on sending image and cache's path(relate path).
 
 - **homeSystem**
 
 ```sql
serial varchar(50) primary key,
petCount int default 1
 ```

 This table is used to manage pet-home's information. Specially serial is very important to use or search other data.
 
 - **request**
 
 ```sql
serial varchar(50),
requestor varchar(50),
request varchar(50),
FOREIGN KEY (serial) REFERENCES homeSystem (serial)
 ```
 
 This table is used to manage pet-home's request list. If a user(registed user) request any operation(s), this server will save it.
After a pet-home request to its works in database, server will send this list and delete this tuple. This tuple is pet-home's works.


## Membership Management

The step of user registration is below steps.

1. User must write a keyword;```등록``` in messager app(NaverTalkTalk).
2. A user-Key of user writting keyword ```등록``` and temporary ID that created by IDissuance module is registed in TempID table.
3. This server send a link ```https://url/signup/<temporary-ID>```that created by auth module and reply module.
4. If the user click this link, user registration form will be shown. User will fill this form.
5. If the user send form, this server check this user's temporary ID and start the step of registration.
6. In step of registration, this server delete ```TempID``` tuple that exist the temporary ID.
7. In next step, this server add the data of registration form in ```naverUser``` table and ```homeSystem``` table.


## Note

 - Apply from public IP to HTTPS
   1. [AWS EC2 setting guide](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md)
   2. [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)
   3. [How to use SSL Certificates and apply HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS.md)
