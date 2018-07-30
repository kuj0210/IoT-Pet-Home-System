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
def optFlow(self, frame. prvs. hsv)
```
- input: frame(frame), prvs(frame), hsv
- outpu: prvs(frame), new hsv, bgr(frame)
- description: Detection of Moving Objects in an Image Using the Dense Optical Flow of OpenCV

```python
def getCenterOfContour(self, image)
```
- input: optical flow image
- output: insert center points into optical flow image
- description: Use the optflow () to retrieve the center point of the contour by acquiring the contour in the detected image.
   
```python
def capture(self)
```
- output: Generate current frame as 'model name' + '.PNG' file
- description: Creates an image file in png format with model name.

```python
def signalHandler(self, signum, frame)
```
- description: Safe shutdown function to be performed on signal
   
```python
def register_all_signal(self)
```
- description: Performs a signalHandler on all signals.
   
```python
def modeFinder(self, list)
```
- input: A collection of areas where pets are found(list)
- description: Sorts the values in the list in descending order by frequency and returns a new list containing the frequencies.
   
```python
def areaDetection(self, x, y)
```
- input: center point
- description: Function to find the position of a center point in a partition of an image
   
```python
def petTracking(self)
```
- description: Using the above functions, periodically observe the movements of animals and give an alarm if they are not visible for a given time.

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



 ## **LICENSE**
 
 IoT-Pet-Home-System's pet-home is licensed under [BSD 3-Clause License](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/PetHome/LICENSE).
 
 ```
Copyright (c) 2018-present, kuj0210, KeonHeeLee, seok8418
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
 
 
 
