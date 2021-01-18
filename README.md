# Instagram

#### Author: [Ariso Okanga](https://github.com/Arisodee)

## Description
This web application allows users to sign up, upload their pictures, view pictures posted by other users, comment on the pictures and like them

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if you have an account | If you dont have , click on sign up and fill the form  | Upon successful login, user is navigated to the home page | Edit profile | Click on the  update profile on the account link | Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Comment and like on a post | Click on the comment and like icon and add a comment and like | The comment and like will be added to the posts | Add new post | Click on the New Post icon to be redirected to the new post form | the post will be rendered to the home page
| Click on log Out in the accounts | Redirects to the login form | user is logged out |


## Features
- User can view images 
- User can see all images per location they were taken
- User can also search for images based categories
- Admin can upload images from the django dashboard

### Link to Live Site 
- [Instagram](https://ariso-insta.herokuapp.com/)


## Technologies Used
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku

### Prerequisite
This project requires a prerequisite understanding of the following:
- Django Framework
- Python3.6
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repository
####  Activate virtual environment
Create and activate virtual environment using python3.6 as default handler
    `python3.6 -m venv virtual && source virtual/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE instagram;
####  .env file
Create a file named`.env`  and copy paste the following filling-in where appropriate:
```
SECRET_KEY='nzq3mylg3#%gd892-fzj@nv%5dr12d33bzzse_&5_zt#l-@(4b'
DEBUG=True
DB_NAME='instagram'
DB_USER='<your database username>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```
#### Run initial Migration
python3.6 manage.py makemigrations instagram
python3.6 manage.py migrate

#### Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

## Known bugs
No known bugs at the moment

## Support and contact details
Incase you come across errors, have any questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at : arisodee@gmail.com

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)