### Hood Experience
This is an Independent project for Moringa Core Django module, september 24 2021.

## Author
Awadh Said

### Description
A web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

### features
As a user I would like to
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

### Deployed link
[Live link](https://hoodexperience.herokuapp.com/)

##### Cloning the repository:

[Repo](https://github.com/Awadh-Awadh/hoodExperience)

#### Install and activate Virtual
 ```bash 
-  - pipenv shell 
```  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
#### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations <database name>
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 

### run app
 ```bash 
 python manage.py runserver 
```  
##### Runing the application 
 ```bash 
 python manage.py runserver
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.1](https://docs.djangoproject.com/en/3.0/) 
* [Heroku](https://heroku.com)  
* [Git](for version control)

## License

- Licensed under[MIT license](license).
