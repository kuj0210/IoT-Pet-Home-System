# db module

This module handle database and data related to this system.

## Module query (directory)

Modules in this directory are those that manage queries for ```MySQL```.

## Module dbcon

This module is a module that stores the information that will be used to access the database. <br>
It is recommended to modify and use as needed.

## Module Register

### class Register

This class focuses on how to manage the database according to requests from users or systems.
The database must be managed through this class in which the database 
will need in this system and a group of roles is created by combining the queries required from the ```query``` module.

```python
def connectDB(self)
```

  - **description**: This method connect to database by referring to dbcon module. 
  If there is no a database called ```SystemData```  in MySQL, create it.

```python
def checkUserTable(self)
```

  - **description**: This method check if there is a table called ```naverUser``` If not, create.

```python
def checkSystemTable(self)
```

  - **description**: This method check if there is a table called ```homeSystem``` If not, create.
  
```python
def checkRequestTable(self)
```

  - **description**: This method check if there is a table called ```request``` If not, create.

```python
def checkTempIdTable(self)
```

  - **description**: This method check if there is a table called ```TempID``` If not, create.

```python
def checkSavedImageTable(self)
```

  - **description**: This method check if there is a table called ```OldImageList``` If not, create.
  
```python
def openDB(self)
```

  - **description**: First, this method connect to MySQL. And then check each tables. 
  Afterwards, we will be able to manage and manipulate the database.

```python
def closeDB(self)
```

  - **description**: Close cursor and connection of database.

```python
def checkRegistedUserForOuter(self, user_key)
```

  - **input**: user_key(string)
  - **output**: isRegistedUser(boolean)
  - **description**: This method is created to check if a user exists outside (in an external block). If a registered user is correct, 
  the method has a ```True``` or ```False``` structure. (Is there a corresponding ```user_key``` in the table named ```naverUser```?)
  
```python
def checkRegistedUser(self, user_key)
```

  - **input**: user_key(string)
  - **output**: isRegistedUser(boolean)
  - **description**: Unlike the method called ```checkRegistedUserForOuter```, 
  this method checks whether the user(by ```user_key```) has registered internally or not. 
  Although the previously described methods are written externally, ```openDB()``` and ```closeDB()``` 
  are used both internally and this method don't require the previous two. Returns ```True``` or ```False``` if a registered user. 
  ( Is there a corresponding ```user_key``` in the table named ```naverUser```?)

```python
def checkRegistedSerial(self, serial)
```

  - **input**: serial(string)
  - **output**: isRegistedSerial(boolean)
  - **description**: This method distinguishes between registered ```serial``` from within a class. 
  If the ```serial``` is registered, return ```True``` or the ```False```.
  ( Is there a corresponding ```seiral``` in the table named ```homeSystem```?)

```python
def checkTempIDByTempID(self, tempID)
```

  - **input**: tempID(string)
  - **output**: isRegistedTemporaryID(boolean)
  - **description**: This method identifies if a temporary issued ID(```tempID```) exists in a table named ```TempID```. 
  If present, return ```True``` or ```False```.  (Is there a corresponding ```ID``` in the table named ```TempID```?)
  
```python
def insertUserData(self, user_key, serial, email, petname)
```

  - **input**: user_key(string), serial(string), email(string), petname(string)
  - **output**: Message of whether user registration is normal (string)
  - **description**: This method is first checked to see if the ```user_key``` that has been parameterized is already registered. 
  If the user is registered, the registered user is notified(```exception.NO_REGISTERD_SERIAL```). 
  If not, insert the data into the table(```naverUser```). 
  And it tells you that you succeeded(return ```reply.SUCESS_IST_USER```). 
  If you fail, return the message(```exception.DONT_REGIST```) that you have failed.
  
```python
def insertUserRequest(self, user_key, request)
```

  - **input**: user_key(string), request(string)
  - **output**: Message of whether request reception to pet-home is normal (string)
  - **description**: This method checks if a user has already been registered with the ```user_key``` received as a parameter, 
  otherwise it is not registered(```exception.NO_REGISTERD_USER```). If you are a registered user, 
  use the key named ```user_key``` to obtain a ```serial``` from the table named ```naverUser```. 
  Then, insert the parameter ```request``` into the ```request```(table) 
  and inform the successful request(```reply.SUCESS_RECEVIED_MSG```). 
  If it fails, it will be notified that it is an unsupported function(```exception.UNSUPPORTED_TYPE_COMMAND```).
  
```python
def fetchRequest(self, serial)
```

  - **input**: serial(string)
  - **output**: Command list(string) if successful. If not, state value(None) as a result of failure
  - **description**: This method first checks for existing keys using ```serial``` keys 
  and notifies if or not registered serial(```exception.NO_REGISTERD_SERIAL```).
  If a registered ```serial```, fetch the ```request``` key from the ```request``` table using ```serial```. 
  If the value of the request is present, proceed to the next step, but otherwise, return ```False```. 
  Then, clear the tuple corresponding to the ```serial``` from the ```request``` table 
  and return the request list(```self.listToString(rows)```). In case of failure, simply terminate the method.
  
```python
def deleteUserData(self, user_key)
```

  - **input**: user_key(string)
  - **output**: Result message for that method(string)
  - **description**: Method for deleting users. First, check if the user is registered, and then inform the registered user 
  if not regist user(```reply.SUCESS_DEL_NO_REGISTERD_USER```). Delete the tuple corresponding to the ```user_key``` 
  and notify it(```reply.SUCESS_DEL_REGISTERD_USER```). If this process fails, 
  inform you that it has failed(```exception.DEL_REGISTERD_USER```).
  
```python
def deleteTempID(self, tempID)
```

  - **input**: tempID(string)
  - **output**: isSuccessToDeleteTemporaryID (boolean)
  - **description**: This method first checks if the user is registered with a temporary ID(```tempID```) and if not, 
  returns ```False```. If the temporary ID is issued, delete the tuple from the ```TempID``` table using the key called ```tempID```. 
  And return ```True```. If this process fails, it returns ```False```.
  
```python
def updatePetCount(self, user_key, petCount)
```

  - **input**: user_key(string), petCount(string)
  - **output**: isSuccessToUpdatePetCount (boolean)
  - **description**: This method first obtains the key named serial from ```user_key```. 
  Then check the registered ```serial``` and if registered serial, 
  update the ```petCount``` of the tuple corresponding to the ```serial``` in the ```homeSystem``` table. 
  If this process is successful, it returns ```True```, or ```False``` if it fails.
  
```python
def getSerialFromUser(self,user_key)
```

  - **input**: user_key(string)
  - **output**: serial(string);success or status message(string or False(boolean));fail
  - **description**: This method is checked from ```user_key``` to determine if it is a registered user. 
  If not, notify that it has not been registered(```exception.NO_REGISTERD_USER```). 
  Then obtain the ```serial``` key from the ```naverUser``` table using the ```user_key```. 
  Then return the value(```rows[0][0]```). Returns ```False``` if the key is not present, 
  or exception message(```exception.SELECT_FROM_CHECKING_SERIAL```) if the key fails in the process of obtaining it. 
  The method is used internally within the class.
  
```python
def getUserFromSerial(self, serial)
```

  - **input**: serial(string)
  - **output**: user_key(string);success or status message(string or False(boolean));fail
  - **description**: This method first checks the registered ```serial```. If not registered, notify(```exception.NO_REGISTERD_SERIAL```).
  If successful, use the ```serial``` key from the ```naverUser``` table to obtain the ```user_key```. 
  Returns ```False``` if no lookup results are found and gets the ```user_key list```(```self.listToString(rows)```) if successful. 
  If the retrieval process fails, an exception message(```exception.SELECT_FROM_CHECKING_USER```) is returned.
  
```python
def getPetCountFromSerial(self,serial)
```

  - **input**: serial(string)
  - **output**: petCNT(int) or status value(string or -1(int))
  - **description**: This method first performs a registered ```serial``` check. 
  If not, return the corresponding message(```exception.NO_REGISTERD_SERIAL```). 
  If yes, obtain ```petCount``` using a ```serial``` within the ```homeSystem``` table. 
  Then return this value(```petCNT```). If failed, return ```-1```.
  
```python
def insertTempID(self, user_key, id)
```

  - **input**: user_key(string), id(string)
  - **output**: If failed, return status value(string or False(boolean))
  - **description**: This method checks if it is a registered user(using ```user_key```). 
  If registered, return ```False```. If not, place ```user_key``` and ```id```(```tempID```) in ```TempID``` table. 
  If this process fails, a status message(```exception.DONT_REGIST```) is returned.
  
```python
def getUserKeyByTempID(self, tempID)
```

  - **input**: tempID(string)
  - **output**: user_key(string)
  - **description**: This method obtains ```user_key``` from the ```TempID```. If it fails, return ```None```.
  
```python
def listToString(self,list)
```

  - **input**: list(list)
  - **output**: str(string)
  - **description**: This method serves to convert the list(```list```) into a string(```str```). 
  It is mainly used to make lists easier to handle.
  
