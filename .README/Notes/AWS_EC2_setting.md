# AWS EC2 setting guide

## 0. First.. <br/>

- You can have your own way of using what you want to use AWS EC2.
- But if you want to build a server for testing or simply, use a "free tier".
- Some countries limit their countries depending on messenger platform servers. <br/>
  Therefore, you can get to know the area and choose it. (The area we use is Seoul.)
  
  <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im01.PNG">
  
  <Img01 : Selection(the top right) image : Asia Pacific (Seoul) >
  
- The AWS cloud service has many features that are useful. But we will also explain how to set up a server <br/>
  and see the links below for more details. <br/>
  + detail(language : korean) : https://aws.amazon.com/ko/getting-started/use-cases/
  

## 1. Create an instance

- **First,** you'll see the screen below on page AWS EC2, and click the "Create Instance" button in the middle.

<img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im02.PNG">

  <Img02 : Please click on the spot marked with red.>

- **Second,** Before you create an instance, you will see a window to choose which operating system you will use. <br/>
  You can select the operating system that you want to use here. <br/>
  (Note that the operating system that we use is using ubuntu 16.04.)
  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im03.PNG">

  <Img03 : Select operating system>
  
- You can pass the process one after another. <br/>
  (The settings vary depending on the rate policy. Please check and select.)
- If you enter the Instances category on the left and see the screen below, you have created an instance normally.<br/>
  Now wait for the operating system to be installed on the instance and you can use that instance <br/>
  when the instance status becomes "running."
  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im04.PNG">

  <Img04 : The screenshot of "instance" category>
  
  
## 2. Get Elastic IP

- The screenshot below is a "Elastic IP" management category.
  If you want to generate a elastic IP, you can click on the button labeled red (blue button: Allocate new address).


  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im05.PNG">
  
  <Img05 : The screenshot of "Elastic IP" category">
  
- Additional creation of elastic IP would likely follow the billing framework set by AWS.

  
## 3. Connect instance and elastic IP

- **First,** you must click the elacstic IP and and "connect address".

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im06.PNG">

<Img06 : Click this.>

- **Second,** Select the instance ID to use, select the internal IP (private IP),<br/>
  and press the "Connect" button to connect the instance with the elastic IP.
  
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im07.PNG">

<Img07: You can use the window above with a selection.>


## 4. Inbound Rules Settings

- Following the settings above, a full communication (TCP based communication) is possible, <br/>
  but further use of other ports from outside is not allowed. Because of this, you must open the port using inbound rules.
- Click on the security group for that instance in the screenshot below.
  
  
  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im08.PNG">
  
  <Img08 : Let's select a security group.>
  
- In the selected security group, click on the item titled "Edit Inbound Rule".

 <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im09.PNG">
 <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im10.PNG">
 
 <Img09,10 : Click "Edit Inbound Rule".>
 
- The screenshot below was taken as a reference and will default to HTTP and SSH only.<br/>
  Therefore, we can open port 443(using for HTTPS) by clicking on the " Add Rule " button.
  
  <img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/aws_ec2_setting_im11.PNG">
  
  <Img11 : Description Inbound Rule>
  
  
## Finally..

In addition, PuTTY and WinSCP can be used to access the above instances. After creating an instance,<br/>
we can get a key for that instance. The key can also be changed to a key that can be used for PuTTY and WinSCP using PuTTYgen.<br/>
<br/>
If you have any questions regarding the AWS EC2 establishment method described above, I would appreciate it <br/>
if you leave an article in the Issue category.<br/>



## Notes

1. [PuTTY Download link](https://www.putty.org/)
2. [WinSCP Download link](https://winscp.net/eng/download.php)

**(1) AWS EC2 setting description(about instance & public IP)**<br/>
(2) [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)<br/>
(3) [How_to_use_SSL_Certificates_and_apply_HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS.md)<br/>

### Go to [main page](https://github.com/kuj0210/IoT-Pet-Home-System).

