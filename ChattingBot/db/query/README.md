# query module

Modules in this directory are those that manage queries for MySQL.</br>
The following are the rules for querying modules in this directory.

## How to read this modules

```mysql
<Module-name>.<To find>from<Condition>
```

- Two example are shown below.

```python
delete.requestBySerial(serial) # example 1
select.userKeyBySerial(serial) # example 2
```

1. The above **example::1** means that the ```delete``` module finds a key called ```request``` from the ```serial```.<br/>
In other words, this function is equal with ```delte from request.request where homeSystem.serial="serial";```.<br/>
2. The above **example::2** means that the ```select``` module finds a key called ```user_key``` from the ```serial```.<br/>
In other words, this function is equal with ```select user_key from naverUser where naverUser.serial="serial";```.<br/>

Modules are organized by the above rules, and other specific queries in the module ```util```.


## Term Description

Before handling queries, we saw what key they held in the database on Main. <br/>
But you won't know exactly what means its key. I will give an explanation for it.

### **serial** (string):
This is a unique number for the pet home. This value is issued and managed by the DB administrator. There is no value condition.

### **UserKey** (string):
This is a unique number for User.There is no condition, and it is a unique value issued directly by each messenger to distinguish or PUSH the user.

### **Email** (string):
This is a registed user's email. Although they do not currently have a big role, they will be given a specific role in the future.

### **petName** (string):
It is used to indicate the name of the pet home or the name of the pet animal. There are no special places used at the moment, 
but it will be used for future updates to give orders to specific pet homes or pets.

### **petCount** (int):
This is to check how many pets there are.

### **ID** (string):
It was introduced as a temporary identity concept before registering users, before using the ```user_key```. 
User registration is possible only with the temporary ID. See the ```api.IDissuence``` module for rules that generate the ```ID```.

### **addr** (string):
This key identifies which path the temporarily saved image is in.

### **requestor** (string):
Created by the server to find out which user has requested a command from Pet Home.

### **requset** (string):
This key is to what command you want pet home to perform.


## Modules Description

- **create**: Module with query to generate table.
- **delete**: Module collecting queries to delete specific tuples.
- **insert**: Module collecting queries to insert specific tuples.
- **select**: Module with queries to fetch tuples or keys for specific conditions.
- **update**: Module collecting queries to update specific tuples.
- **util**: Module that collects other data necessary to carry out the work or query
