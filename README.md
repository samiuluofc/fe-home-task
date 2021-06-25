# REST api endpoints for the Winnipeg weather data.

### How to run the application locally using docker compose:

Build: $ docker-compose build  
Run: $ docker-compose up  
Remove the database volume: $ docker-compose rm -f db

### Setting up the vitual environment for data creation and test:
$ cd api_service  
$ python -m venv env  
$ .\env\Scripts\activate  
$ pip3 install -r requirements.txt  

### Insert data from a CSV using the POST (/forecast) call:

$ cd api_service  
$ python upload_data.py  

This is just to quickly fill the MongoDB from the provided CSV in this repo. 
This also verify that POST call is working.

###  Quick test/verification on the GET (/forecast) call:

$ cd api_service  
$ python test_get_data.py  

###  Example input in the Web application:

Test 1:    
    Date: 2021-06-16  
    Time: 08:00:00   
Test 2:  
    Date: 2021-06-16  
Test 3:  
    Time: 08:00:00  
