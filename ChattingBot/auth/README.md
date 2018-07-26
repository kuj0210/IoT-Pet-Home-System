# auth modules

## Module IDissuance

### class IDIssuance

```python
def getTempID(self, userKey)
```
  
  - **input**: userKey(string)
  - **output**: Temporary-id(string)
  - **description**: This method binds three characters in the string that make up the ```userKey```. 
  And then, calculate the average of the three characters. Finally, at the end of the string(```Tid```) created, 
  a second of the current time(```sec```) is attached. Return this string(```Tid + str(sec)```).
  
  
 ## Module signup
 
 ```python
 def sigup(temp_user_key, form)
 ```
 
  - **input**: temp_user_key(string), form(string)
  - **output**: user_key(string), isSuccess(boolean)
  - **description**: This function is concerned to save user data to the database after registering on the user registration form.
  If a member has successfully signed up for membership, this server return true(```isSuccess```), if not, return false(```isSuccess```).
  There are 4 step of this process. First, get a key about temporary id(```temp_user_key```)(step 1), put data according to the registration form(```form```) into the db(step 2~3), 
  and clear temporary id(```temp_user_key```)(step 4).
