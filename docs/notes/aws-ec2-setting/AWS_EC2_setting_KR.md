# AWS EC2 setting guide

## 0. 시작하며.. <br/>

- AWS EC2는 자신이 원하는 방식으로 사용할 수 있습니다.
- 그러나 테스트를 위해 서버를 구축하거나 간단하게 구축하려는 경우에는 "프리 티어"을 사용하십시오.
- 몇몇 국가들은 메신저 플랫폼 서버에 따라 사용이 제한됩니다. <br/>
  따라서, 여러분은 그 지역을 알아야 하고 그것을 선택해야합니다. (저희가 사용하는 지역은 서울입니다.)
  
  <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im01.PNG">
  
  <Img01: 선택(오른쪽 상단) 이미지: 아시아 태평양 (서울) >
  
- AWS클라우드 서비스는 유용한 여러 기능을 제공합니다. 하지만 저희는 서버를 설정하는 방법만 설명하겠습니다. <br/>
  자세한 내용은 아래 링크를 참조하십시오. <br/>
  + 상세내용(언어: 한국어) : https://aws.amazon.com/ko/getting-started/use-cases/
  

## 1. 인스턴스 생성

- **First,** 아래의 화면은 AWS EC2페이지에 나타나며, 가운데에 있는 "인스턴스 시작"버튼을 클릭합니다.

<img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im02.PNG">

  <Img02: 빨간 색으로 표시된 지점을 클릭하십시오.>

- **Second,** 인스턴스를 생성하기 전에 사용할 운영 체제를 선택할 수 있는 창이 나타납니다. <br/>
  여기서 사용할 운영 체제를 선택할 수 있습니다. <br/>
  (참고로 저희가 사용하는 운영체제는 ubuntu 16.04.입니다)
  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im03.PNG">

  <Img03: 운영체제 선택>
  
- You can pass the process one after another. <br/>
  (설정은 비용 정책에 따라 다릅니다. 확인하고 선택하십시오.)
- 왼쪽에 인스턴스 범주를 입력하고 아래 화면을 보면 인스턴스가 정상적으로 생성된 것입니다.<br/>
  이제 운영 체제가 인스턴스에 설치될 때까지 기다리면 인스턴스 상태가 "실행"상태일 때 해당 인스턴스
  를 사용할 수 있습니다. 
<br/>

  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im04.PNG">

  <Img04: "인스턴스" 항목 스크린샷>
  
  
## 2. Elastic IP 얻기

- 아래 스크린 샷은 "Elastic IP"관리 항목입니다. 
  Elastic IP를 생성하려는 경우, 빨간 색으로 표시된 버튼을 클릭하면 됩니다(파란 색 버튼: 새 주소 할당).


  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im05.PNG">
  
  <Img05: "Elastic IP" 항목 스크린샷">
  
- 추가적인 Elastic IP생성은 AWS에 의해 설정된 청구 프레임워크를 따르는 것 같습니다.

  
## 3. 인스턴스 연결과 Elastic IP

- **First,** 탄력적 IP를 클릭하고, "주소 연결"을 클릭합니다.

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im06.PNG">

<Img06: 주소연결 클릭.>

- **Second,** 사용할 인스턴스 ID를 선택하고 내부 IP(비공개 IP)를 선택합니다.<br/>
  그리고 "연결"버튼을 눌러 인스턴스를 Elastic IP에 연결합니다.
  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im07.PNG">

<Img07: 선택 항목과 함께 위의 창이 사용가능합니다..>


## 4. 인바운드 규칙 설정

- 위의 설정에 따라, 전체 통신(TCP기반 통신)이 가능합니다.<br/>
  그러나 외부에서 다른 포트를 더 이상 사용할 수 없습니다. 이 때문에 인바운드 규칙을 사용하여 포트를 열어야 합니다.
- 아래 스크린 샷에서 해당 인스턴스에 대한 보안 그룹을 클릭하십시오.
  
  
  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im08.PNG">
  
  <Img08: 보안 그룹을 선택합시다.>
  
- 선택한 보안 그룹에서 "인바운드 규칙 편집"항목을 클릭합니다.

 <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im09.PNG">
 <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im10.PNG">
 
 <Img09,10: Click "Edit Inbound Rule".>
 
- 아래 스크린 샷은 참조용으로 작성되었으며 HTTP및 SSH전용으로 기본 설정됩니다.<br/>
  따라서"규칙 추가"버튼을 눌러 포트 443(HTTPS에 사용)을 열 수 있습니다.
  
  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im11.PNG">
  
  <Img11: 인바운드 규칙 설명>
  
  
## 마치며..

또한 PuTTY및 WinSCP를 사용하여 위의 인스턴스에 액세스 할 수 있습니다. 인스턴스를 생성한 후에는 해당 인스턴스에 대한 키를 가져올 수 있습니다.<br/> 이 키는 PuTTYgen를 사용하여 PuTTY및 WinSCP에 사용할 수 있는 키로 변경할 수도 있습니다.<br/>
위에서 설명한 AWS EC2설정 방법에 대해 질문이 있는 경우, 이슈에 글을 남겨주시면 감사하겠습니다. <br/>



## 참고

1. [PuTTY Download link](https://www.putty.org/)
2. [WinSCP Download link](https://winscp.net/eng/download.php)

**(1) AWS EC2 setting description(about instance & public IP)**<br/>
(2) [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting_KR.md)<br/>
(3) [How_to_use_SSL_Certificates_and_apply_HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS_KR.md)<br/>

### [main page](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/README_KR.md)로 이동.
