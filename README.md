# stackoverflow-lite_api-with-database

StackOverflow-lite_Api is an interface that comprises of a set of endpoints that uses a Postgres database to store and query data

### Tools

* Text editor where we write our project files. (VScode)
* Python
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

## Getting Started
clone the github repo to your computer:
* $git clone https://github.com/Rhytah/stackoverflow-lite_api
* Extract the zip file to another file

**Create virtual environment and activate it**
```
$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
``` 
 **Install all the necessary tools by**
 ```
 $pip insatll -r requirements.txt
 ```
**Start app server in console/terminal/commandprompt**
```
$python run.py
```
## Versioning
```
This is version one"v2" of the API
```
## End Points
|           End Point                               |            Functionality                   |
|   ------------------------------------------      | ----------------------------------------- |    POST api/v2/auth/signup                        |             Register User               |
|    POST api/v2/auth/login                         |             User login                  |
|     GET  api/v2/questions                         |             Fetch all questions         |
|     GET  api/v2/questions/<int:question_id>       |             Fetch a question            |
|     POST api/v2/questions                         |             Add a question              | 
|     DELETE api/v2/questions                       |             Delete a question           |     |
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/54ad26ca67837aa2a626)

## Author
- [Rhytah] https://github.com/Rhytah



