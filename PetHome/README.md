# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/RaspberryPi_Logo.jpg?raw=true" width="64">Raspberry Pi Setting

## **Install Rasbian**

 - Installation method of Rasbian<br>
   https://www.raspberrypi.org/documentation/installation/installing-images/

## **How to use Raspberry Pi Camera**

1. Install the Raspberry Pi Camera module by inserting the cable into the Raspberry Pi. 
The cable slots into the connector situated between the Ethernet and HDMI ports, 
with the silver connectors facing the HDMI port.

2. Boot up your Raspberry Pi.

3. From the prompt, run "sudo raspi-config".
```
sudo raspi-config
```

4. If the "camera" option is not listed, you will need to run a few commands to update your Raspberry Pi. 
Run "sudo apt-get update" and "sudo apt-get upgrade"
```
sudo apt-get update
sudo apt-get upgrade
```

5. Run "sudo raspi-config" again - you should now see the "camera" option.
![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Enable_Camera.png?raw=true)

6. Navigate to the "camera" option, and enable it. Select “Finish” and reboot your Raspberry Pi.


   
## **How to connect motor wires**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/raspberry-pi-pinout.png?raw=true)


### Food Motor

- Orange wired: connects to pin 35
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

### Door Motor

- Orange wired: connects to pin 12
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)


## **Class Description**

### Module server

```python
def parshResponseByNL(self, res)
```
 
```python
def parshResponseBySP(self, res)
```

```python
def loadSerail(self)
 ```
 
```python
def bootUp(self)
 ```
 
```python
def getRequest(self, wating)
```
 
```python
def runMobile(self)
```
 
 
### Module push
```python
def setUpObserverList(self)
```
 
```python
def setUpThread(self)
```
 
```python
def insertMSG(self, user, str)
```
 
```python
def getMSG(self)
```
 
```python
def startTh(self)
```

### Module observer
```python
def reSet(self, push)
```

```python
def run(self, push)
```

```python
def insertRQ(self, user, msg)
```

```python
def popRQ(self)
```

### Module Vi

```python
def optFlow(self, fra,e. prvs. hsv)
```

   Detection of Moving Objects in an Image Using the Dense Optical Flow of OpenCV

```python
def getCenterOfContour(self, image)
```

   Use the optflow () to retrieve the center point of the contour by acquiring the contour in the detected image.
   
```python
def capture(self)
```
   Creates an image file in png format with model name.

```python
def signalHandler(self, signum, frame)
```
   Safe shutdown function to be performed on signal
   
```python
def register_all_signal(self)
```
   Performs a signalHandler on all signals.
   
```python
def modeFinder(self, list)
```
   Sorts the values in the list in descending order by frequency and returns a new list containing the frequencies.
   
```python
def areaDetection(self, x, y)
```
   Function to find pet in any of the segmented areas in the image
   
```python
def petTracking(self)
```
   Using the above functions, periodically observe the movements of animals and give an alarm if they are not visible for a given time.

### Module Translator
```python
def getIMAG_URL(self, user)
```

```python
def getPostBodyMessage(self, user, text)
```

```python
def sendMsg(self, url, user, msg)
```

```python
def pushToUser(self, user, msg)
```

```python
def pushToAllUser(self, msg)
```

```python
def pushImage(self, user, path)
```

### Module FeedOperation

   The class that drives the feed motor

### Module DoorOpeartion

   The class that drives the door motor


