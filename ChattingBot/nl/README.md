# nl module

This module analyze Nature Language(Korean) and pick main keyword for operating each pet-homes or replying to user.

## Module keyword

### class KeyWord

```python
def isMe(self,sentence,originLIST)
```

  - **input**: sentence(string), originLIST(list)
  - **output**: isSuccessToParseNL (boolean)
  - **description**: This method compares keywords divided by KoNLPy(```originLIST```) and original sentence(```sentence```). 
  If the result is analyzed correctly, return ```True``` or ```False```. It is the role of this method to check 
  if a chatbot in question is recognized as a command.

```python
def _print(self)
```

  - **description**: This method is a function that outputs set keywords(by methods;```setNouns(self,list)```,
  ```setVerbs(self,list)```). It is used for testing purposes.

## Module usecase_finder

### class UsecaseFinder

```python
def getNV(self, sentence)
```

  - **input**: sentence(string)
  - **description**: This method analyzes the makeup using the ```KoNLPy``` module 
  and puts the appropriate keywords in the parsing lists(```parsingNVLIST``` and ```parsingLIST```).
  A suitable keyword here is '```noun(명사)```', '```verb(동사)```', '```and(과,와)```'.

```python
def setUserSetting(self)
```

  - **description**: This method is to insert ```keywords``` to be applied in this chatbot.

```python
def printList(self)
```

  - **description**: This is a method used for testing. Print the ```items``` in ```self.usescase```.

```python
def analyzeSentence(self, sentence)
```

  - **input**: sentence(string)
  - **output**: request(list)
  - **description**: This is a function that checks the fit of ```keyword```s and puts them in the ```request``` list if appropriate. 
  In other words, ```keyword```s are extracted from chatbots for command or pet-home operation commands.

```python
def setUsecase(self, name, nList, vList, gravity)
```

  - **input**: name(string), nList(list), vList(list), gravity(int)
  - **description**: This method sets keyword(```name```) to extract to use on commands or pet-home operations,
  nouns(```nList```), verbs(```vList```), and the weight(```gravity```) to distinguish between them to extract keywords. 
  A list created using that method will be extracted to see if there are suitable keywords.

## util

 This method is a module used to store weights to be used in the ```UsecaseFinder``` class.
