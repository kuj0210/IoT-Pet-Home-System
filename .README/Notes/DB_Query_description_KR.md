# DB Query description (MySQL)

저희 시스템은 pet home과 사용자 등록으로부터 오는 정보를 다루기 위해서 MySQL을 사용합니다.<br/>
이를 위해 저희는 두 개의 DB테이블을 처리하며 상세 쿼리는 다음과 같습니다 :


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

- USERdata는 테이블을 저장하기위한 데이터베이스입니다.<br/>

<**왜 utf-8을 사용하는가?** 한글을 처리할 수 있기 때문에 utf-8로 설정했습니다.>


## 2. Create or Use Tables<br/>

### 2-1. homeSystem table<br/>

우선 homeSystem 테이블이 존재하는지 확인해야 합니다. 따라서 아래 쿼리를 사용하십시오.<br/>

```
select * from homeSystem;
```

오류가 발생한다면 homeSystem 테이블이 없는 것이므로 새 테이블을 생성하십시오.
(이 오류는 결과가 없는 것과는 다릅니다. 결과가 없는 것은 테이블에 데이터가 없을 뿐입니다.)

```
create table homeSystem(
       PiKey varchar(50),
       Platform varchar(30),
       Email varchar(50),
       url varchar(50)
       ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
```

- 이 테이블에는 장치에 등록해야 하는 사용자에 대한 정보와 장치가 속하는 URL, 장치의 키값이 포함되어 있습니다.<br/>
- 이 테이블의 장치와 연관되어 있으므로 이 테이블에 대한 데이터가 없는 것은 등록된 장치가 없는 것과 같습니다.
  
  
### 2-2. %%%%%User<br/>
(%%%%%는 플랫폼의 이름입니다. NULL(NaN))이 아닙니다.<br/>

우선, 우리는 그 테이블들이 존재하는지 확인해야 합니다. 그러므로 아래의 쿼리를 사용하십시오.
```
select * from kakaoUser; # This query is used to kakao-talk platform.
select * from naverUser; # This query is used to naver-talk-talk platform.
```

오류가 발생하면 %%%%%User 테이블이 없으므로 새 테이블을 생성합니다.<br/>
(이 오류는 결과가 없는 것과는 다릅니다. 결과가 없는 것은 테이블에 데이터가 없을 뿐입니다.)

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

- 위의 테이블은 챗봇 플랫폼에 대한 사용자 정보를 포함합니다. <br/>
- 사용자 등록시, "INSERT query" 가 각 플랫폼에 맞게 위 테이블에 배치됩니다.


### 2-3. Use these tables.<br/>

```
select * from homeSystem;

# Please use the queries for each platform.
select * from kakaoUser;
select * from naverUser;
```

우리는 앞서서 만들어온 테이블을 지금은 사용해야합니다. 테이블을 사용하려면 위의 쿼리를 사용하십시오.<br/>
테이블을 본 뒤에, 데이터를 세부적으로 다루기위해서는 서버의 "RegistUser.py" 소스코드를 참조하십시오.


## 3. Insert tuple into table <br/>

### 3-1. insert tuple into homeSystem table.

```
insert into homeSystem values ("PiKey","Platform","Email","url");
```

위의 예는 튜플이 homeSystem 테이블에 삽입된 SQL 문장입니다.<br/>
SQL문은 수동적으로 사용되지 않으며 장치가 켜져 있을 때만 실행됩니다.<br/>


### 3-2. insert tuple into each platform's table.

```
#If platform is "kakao-talk"
insert into kakaoUser values ("user-key","email","kakao-talk");

#else (if platform is "naver-talk")
insert into naverUser values ("user-key","email","naver-talk");
```

각 플랫폼에 대해 위의 SQL문을 사용합니다. <br/>
사용자가 "[등록]" 명령을 사용하는 경우엔, 이 SQL문이 사용됩니다.


## 4. Examples of Using <br/>

**Common point** use database;USERdata. 

```
use USERdata;
```

### 4-1. Check registed user

```
# if platform is "kakao-talk":
select email from kakaoUser where kakaoUser.user_key=user_key;

# else (if platform is "naver-talk")
select email from naverUser where naverUser.user_key=user_key;
```

- 이 쿼리문은 챗봇을 사용하는 사용자가 서버에 등록된 사용자인지 확인하는 데 사용됩니다.


### 4-2. Find URL and PiKey

```
# if platform is "kakao-talk":
select url,kakaoUser.PiKey 
from kakaoUser join homeSystem on kakaoUser.Email=homeSystem.Email 
where kakaoUser.user_key=user_key;

# else (if platform is "naver-talk")
select url,naverUser.PiKey 
from naverUser join homeSystem on naverUser.Email=homeSystem.Email 
where naverUser.user_key=%s;
```

- 이 쿼리문은 대개 장치에 연결할 때 사용됩니다.


### 4-3. Get userlist

```
select naverUser.user_key 
from naverUser join homeSystem on naverUser.Email=homeSystem.Email 
where homeSystem.PiKey=PiKey;
```

- Push알람 기능을 사용할 때는 이 쿼리를 사용하나, <br/>
  현재는 Push알람 기능은 Navertalk만 지원하므로, 위 문장을 사용하십시오.
  
  
### 4-4. Find user e-mail

```
# if platform is "kakao-talk":
select email from kakaoUser where kakaoUser.user_key=user_key;

# else (if platform is "naver-talk")
select email from naverUser where naverUser.user_key=user_key;
```

- 계정을 잊어 버린 경우 이 쿼리문을 사용하십시오.
- [정보]명령을 사용하여 호출되는 쿼리문입니다.


### 4-5. Update homeSystem table.

```
delete from homeSystem where PiKey="PiKey";

# for user in userlist :
#    if email in kakaoUserList :
        insert into homeSystem values ("PiKey", "kakao-talk", "your@email", "url");
        
#    if email in naverUserList :
        insert into homeSystem values ("PiKey", "naver-talk", "your@email", "url");
```

- 이 쿼리문들은 장치가 서버에 연결될 때 사용됩니다.(장치가 켜져 있을 때 작동합니다.)<br/>

<br/><br/>


## 마치며..
만약 당신이 더 나은 쿼리문을 생각하고 Contributor를 얻고 싶다면, Pull requests해주시면 감사하겠습니다!
### [main page](https://github.com/kuj0210/IoT-Pet-Home-System/README_KR.md))로 이동.
