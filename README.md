TO RUN THIS PROJECT SUCCESSFULLY FOLLOW THIS STEPS

1) Download this repo in folder called Ondek
2) In folder before the manage.py setup your virtual env
3) Activate your virtual env then install this following python libs into your virtual env from text file called requirements.txt.
4) create database called ondek (if any other name then make respective changes)
5) Run following commands to migrate changes to database
    python manage.py makemigrations
    python manage.py migrate
6) Create super user
    python manage.py createsuperuser
   Use this login credentials to login into your admin site.
7) SET UP IS DONE NOW YOU CAN RUN FOLLOWING COMMAND TO START YOUR SERVER
    python manage.py runserver
    
-Following are the link for better navigation of the project:
-http://127.0.0.1:8000/admin

-with help of super user create mediators, hospitals, nurses
-then those hospital nurses can create shifts and applications resp.
