# DB Query description (MySQL)

Our system uses MySQL to handle information from pet homes and user registrations.<br/>
To do so, we handle the two DB tables and the detailed query are as follows :


## 1. Create or Use Database <br/>


**if USERdata database is existed**
```
use USERdata;
```

**else** #if not exist USERdata database.
```
create database USERdata
DEFAULT CHARACTER SET utf8 
collate utf8_general_ci;
```

- A database called USERdata is for storing tables.<br/>

<**Why use utf8?**    Because it could handle Hangul, we set it as utf-8.>


## 2. Create or Use Tables<br/>

### 2-1. homeSystem table<br/>

First, we must check whether the homeSystem table exists. Therefore use the query below.<br/>

```
select * from homeSystem;
```

If an error occurs, create a new table as there is no homeSystem table. <br/>
(This error is different from the one without results. No result is just no data on the table.)

```
create table homeSystem(
       PiKey varchar(50),
       Platform varchar(30),
       Email varchar(50),
       url varchar(50)
       ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
```

- This table contains the device key values, information about users who should be registered with the device,<br/>
  and url to which device belongs.<br/>
- Since it is associated with the device in this table, the absence of a data for this table is equivalent <br/>
  to the absence of a registered device.
  
  
### 2-2. %%%%%User<br/>
(%%%%% is platform's name. not NULL(NaN))<br/>

First, we must check whether the tables exist. Therefore use the queries below.

```
select * from kakaoUser; # This query is used to kakao-talk platform.
select * from naverUser; # This query is used to naver-talk-talk platform.
```

If an error occurs, create new tables as there are no %%%%%User tables. <br/>
(This error is different from the one without results. No result is just no data on the table.)

```
create table kakaoUser(
       user_key varchar(50),
       Email varchar(50),
       PiKey varchar(50),
       primary key (Email)
       ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
       # Kakao-talk platform.
 
create table naverUser(
       user_key varchar(50),
       Email varchar(50),
       PiKey varchar(50),
       primary key (Email)
       ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
       # Naver-talk-talk platform.
```

- The tables above contain user information for each Chatbot platform. <br/>
- When the user registers with the user, the "INSERT query" is placed in the table above to fit each platform.


### 2-3. Use these tables.<br/>

```
select * from homeSystem;

# Please use the queries for each platform.
select * from kakaoUser;
select * from naverUser;
```

Since we created the table earlier, we have to use it now. To use the table, please use the query above.<br/>
After looking at the table, please refer o the server's "RegistUser.py" source code to handle the data in detail.


## 3. Insert tuple into table <br/>

### 3-1. insert tuple into homeSystem table.

```
insert into homeSystem values ("PiKey","Platform","Email","url");
```

The example above is the SQL setence where the tuple is inserted into the homesystem table.<br/>
The SQL statement is not used consciously, but only runs if the device is turned on.<br/>


### 3-2. insert tuple into each platform's table.

```
#If platform is "kakao-talk"
insert into kakaoUser values ("user-key","email","kakao-talk");

#else (if platform is "naver-talk")
insert into naverUser values ("user-key","email","naver-talk");
```

For each platform, use the above SQL statement. <br/>
When a user uses the command "[등록]", this SQL statement is used.


## 4. Examples of Using <br/>

**First** use database;USERdata. 
```
use USERdata;
```

**Second** 
