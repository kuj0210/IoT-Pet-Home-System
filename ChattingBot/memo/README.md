# memo module

This module memorize cache related a images recieving from pet-homes and if this cache isn't unecessary, this module delete it.

## Module Cache
This class is a class that manages which ```cache(images)``` to store and erase, depending on the user. 
The main server clears previously used images and stores data from the current pet-home.
In other words, it temporarily saves the images from the pet-homes, pushes them to the users, 
and erases the images previously saved when new images are sent from the pet home.


### class Cache

```python
def memorization (self,key,val)
```

  - **input**: key(string), val(string)
  - **description**: This method stores ```key```s and ```value```s in ```self.memory```, 
  an internal member of this class. Here the ```key``` is the ```serial```
  of the pet-home and ```the name of the file``` to which the ```val``` will store.

```python
 def dememorization (self,key)
```

  - **input**: key(string)
  - **output**: item(string)
  - **description**: This method takes data(file name-```item```) out of cache named ```self.memory```. 
  If an ```item``` corresponding to a ```key``` exists, remove it and erase the ```key```. Otherwise, return False.
  If successful, it returns the normally stored file name(```item```).
