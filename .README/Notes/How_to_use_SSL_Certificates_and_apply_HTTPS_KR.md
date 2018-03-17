# How to use SSL Certificates and apply HTTPS

 HTTP에서 HTTPS로 변경하려면 SSL인증서를 가져와야 합니다. 그리고 이 SSL인증서를 플라스크와 같은 프레임워크에 적용하여 HTTPS를 사용하는 웹 서버를 완료해야 합니다. SSL인증서를 받기위해서 "Let's encrypt" 클라이언트를 사용하는 방법에 대해 설명합니다. 실제로 SSL을 연결하는 프로세스는 우리의 소스 코드(플라스크 기반)에 대한 예를 제공하는 것입니다.<br/><br/>
* 올바른 IP설정이나 도메인 이름이 없는 경우에는 아래에 있는 링크를 통해 설정하고 이 메뉴얼을 읽으십시오.
* 셸(Linux)환경에서 진행하겠습니다.


## 1. Let's Encrypt 설치

```
$ git clone https://github.com/letsencrypt/letsencrypt
````

- " Let's Encrypt "는 이러한 명령을 사용하여 클론으로 가져올 수 있는 오픈 소스 도구입니다.

```
$ cd letsencrypt
$ ./letsencrypt-auto --help
```

- 원본 코드를 가져온 후에는 설치해야 합니다.
- 파일이 있는 디렉토리로 이동합니다.
- 필요한 파일을 자동으로 다운로드 하기 위해서 ```. /letsencrypt-auto —help```을 입력하세요
- ```./letsencrypt-auto —help```를 입력했다면, 설치 후에 사용 방법을 확인 할 수 있습니다. 

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/ssl01.PNG">

<img01: letsencrypt 사용법>


## 2. SSL 인증서 가져오기

```
$ ./certbot-auto certonly --manual
```

- 위에 설명된 대로 입력하면 인증서를 수동으로 적용할 수 있습니다.
- 약관을 주의 깊게 읽고 Y(Yes)를 입력한 다음 도메인 주소, 이메일 주소를 입력하면 정상적으로 발급됩니다.
```
$ ./certbot-auto certonly -a webroot --webroot-path=[path] -d [Your Domain]
```

- 자동으로 실행되도록 하려면 위의 명령을 입력하면 됩니다.
- 수동 또는 자동으로 인증서가 발급된 후에 발급된 경로가 반환됩니다. 이 경로를 기억하셔야 합니다.
- "fullchain.pem"및"privkey.pem"파일의 경로를 기억해야 합니다. 이는 실제 HTTPS가 이 경로에 적용되기 때문입니다.


## 3. HTTPS 적용

 위에서 설명한 바와 같이, 우리는**Flask**, Python프레임워크를 기반으로 한 HTTPS애플리케이션을 설명할 것입니다.
 
 
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/ssl02.PNG">
 
 <img02: SSL인증서가 첨부된 소스 코드>
 
 - 위의 원본 코드와 같이 인증서를 라우팅 하면 HTTPS가 정상적으로 적용됩니다..
 - HTTPS는 포트 번호 443을 사용하므로 포트 번호를 숫자 443으로 변경합니다.


## 4. SSL인증서 갱신

```
$ ./crontab -e
```

- 위 방법은 SSL인증서를 자동으로 업데이트하는 명령입니다.
- SSL인증서는 3개월에 한번씩 갱신해야 하므로 번거롭다면 위의 명령을 실행해 보십시오.
- 수동으로 갱신하려면 certbot-auto를 사용하십시오.


## 마치며..

 이제 공식 IP주소, 도메인 이름 설정, SSL인증서 발급 및 HTTPS적용에 대해 살펴보았습니다. 적용되지 않거나 의문 사항이 있으시면, 그것을 이슈로 남겨두세요!<br/>
<br/>
<br/>
(1) [AWS EC2 setting description(about instance & public IP)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting_KR.md)<br/>
(2) [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting_KR.md)<br/>
(3) **How to use SSL Certificates and apply HTTPS**<br/>

### [main page](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/README_KR.md) 이동.
