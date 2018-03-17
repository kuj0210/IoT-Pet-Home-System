# Domain setting description

이 메뉴얼에서는 HTTP를 HTTPS로 무시하기 전에 반드시 거쳐야 하는 도메인 주소 변경 사항을 설명합니다.<br/>
It also refers to how to use the "[freenom](https://my.freenom.com/clientarea.php)" 사이트 to change the domain address to handle the process. <br/>
인증된 IP가 있는 경우 이 프로세스를 수행할 수 있습니다. (공인 IP가 없는 경우 [설명]참조)(https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md).)


## 1. 회원가입

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img01.PNG">

<img01: 회원가입 페이지>

- 여기서 등록할 수 있지만, 저는 구글 계정으로 로그인 하겠습니다.
- 회원 가입 시 몇가지 조건과 결제 방법이 있습니다. <br/>
  그 부분은 자발적으로 선택할 수 있습니다.
  

## 2. 도메인 찾기

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img02.PNG">

<img02: "Register a New Domain" 선택.>

- 오른쪽 위 모서리에 "Services"(서비스)메뉴가 나타납니다. 여기서 "Register a New Domain" 카테고리를 클릭합니다.


<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img03.PNG">

<img03: 새로운 도메인 찾기.>

- 이 과정은 도메인을 사용할 수 있는지 확인하는 것입니다. 원하는 도메인 주소를 적어 주세요.
- 일부 도메인에는 요금이 부과되기 때문에, 가능하다면 ".com",".net"과 같은 것들은 피하십시오.
- 저희는 "testfreenommm"으로 진행했습니다.


<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img04.PNG">

<img04: 이용할 수 있는 무료 도메인>

- 당신의 도메인을 적으면, 다음과 같은 사용 가능한 도메인을 볼 수 있습니다.
- 위의 스크린 샷과 같이 일부 도메인은 무료지만, 원하는 경우엔 유료 도메인도 사용할 수 있습니다.


<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img05.PNG">

<img05: Get it now!>

- 도메인에 관심이 있으면 "Get it now!"를 클릭하고 위의 스크린 샷에 있는 빨간 색 사인을 확인하세요.


## 3. IP 주소 등록

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img06.PNG">

<img06: 당신이 가지고 있는 공용 IP를 넣어 봅시다.>

- 위 스크린 샷과 마찬가지로 호스트 이름에 해당하는 IP주소를 입력하는 열과 사용할 기간을 입력하는 곳이 있습니다.
- 대개 무료 도메인은 최대 12개월 동안 무료로 사용할 수 있습니다.
- IP주소 칸에는 공용 IP가 포함되어 있어야 합니다.


<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img07.PNG">
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img08.PNG">

<img07,08: 확인 후 세부 정보 입력>

- 위에 나온 것처럼 비용이 얼마나 들지 한번 봅시다. (위의 경우 무료입니다.)
- 세부 정보를 입력하면 도메인 등록이 끝납니다.


<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/freenom_img09.PNG">

<img09: 도메인 등록>

- 위 스크린 샷과 같이 도메인 주소를 확인할 수 있습니다.



## 마치며..

 HTTPS를 사용하려는 부분에 도달했습니다. 도메인 주소를 잘 기억하시기 바랍니다.<br/>
그리고 도메인 주소를 설정하는 방법에 대한 설명을 마치겠습니다. 다음으로 SSL인증서를 발급하는 방법에 대해 설명하겠습니다.

(1) [AWS EC2 setting description(about instance & public IP)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting_KR.md)<br/>
(2) **Domain setting description**<br/>
(3) [How to use SSL Certificates and apply HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS_KR.md)<br/>

###[main page](https://github.com/kuj0210/IoT-Pet-Home-System/README_KR.md)로 이동.
