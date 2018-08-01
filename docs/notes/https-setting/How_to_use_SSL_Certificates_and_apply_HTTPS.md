# How to use SSL Certificates and apply HTTPS

 You must obtain an SSL certificate before you can change from HTTP to HTTPS. And you have to apply this SSL certificate to a framework like flask to complete the web server with HTTPS. We will discuss how to use "Let's encrypt" client to get an SSL certificate. The process of actually plugging in SSL would be to give you an example of our source code (flask based).<br/><br/>
* If you do not have a valid IP setting or domain name, please set it up through the links at the bottom and read this manual.
* We will proceed in a shell(Linux) environment.


## 1. Install Let's Encrypt

```
$ git clone https://github.com/letsencrypt/letsencrypt
````

- The " Let's Encrypt " is an open-source tool that can be imported into a clone using these commands.

```
$ cd letsencrypt
$ ./letsencrypt-auto --help
```

- After you import the source code, you must install it.
- Let's go to the directory where the files are located.
- Enter ```. /letsencrypt-auto --help``` to download dependent-related files automatically.
- If you type ```./letsencrypt-auto --help``` after installing, then you'll see how to use it.

<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/ssl01.PNG">

<img01 : How to use letsencrypt>


## 2. Get SSL Certificate

```
$ ./certbot-auto certonly --manual
```

- If you enter as instructed above, it is a manual method to apply the certificate.
- Read the Terms and Conditions carefully and enter a Y(Yes), then type in the domain address, email address, and you will be issued normally.

```
$ ./certbot-auto certonly -a webroot --webroot-path=[path] -d [Your Domain]
```

- If you want to be issued automatically, you can type in the above command.
- Manual or automatic, the certificate will return the route issued after it is issued. You should remember this route.
- You must remember "fullchain.pem" and "privkey.pem" files's route. This is because the actual HTTPS is applied through this route.


## 3. Apply HTTPS

 As I explained above, we will describe the HTTPS application based on **Flask**, the Python framework.
 
 
<img src = "https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/ssl02.PNG">
 
 <img02 : Source code with SSL certificate attached>
 
 - If you route the certificate as shown in the source code above, HTTPS is applied normally.
 - HTTPS uses port number 443, so let's change the port number to number 443.


## 4. Renew your SSL Certificate

```
$ ./crontab -e
```

- The above method is a command to automatically update the SSL certificate.
- Because SSL certificates must be renewed every three months, if it is annoying, try the above command.
- If you would like to renew manually, use certbot-auto.


## Finally..

 Now I have looked at the official IP address, domain name settings, SSL certificate issuance, and HTTPS enforcement. If you don't apply or have any questions, please leave it as an issue!<br/>
<br/>
<br/>
(1) [AWS EC2 setting description(about instance & public IP)](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md)<br/>
(2) [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)<br/>
(3) **How to use SSL Certificates and apply HTTPS**<br/>

### Go to [main page](https://github.com/kuj0210/IoT-Pet-Home-System).
