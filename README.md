# Test project for Codecool based on Django.

## How to run example ? 

Run command line and provide below commands (make sure you are in directory with manage.py file) : 
```sh 
$ python manage.py migrate # create necessary files for database manage (default database system is SQLite)
```
```sh 
$ python manage.py runserver 8080 # run server with our application, should works at http://localhost:8080 in web browser
```
## Administration panel: 

If your server is working use Ctrl + C (Cmd + C on Mac) to stop server, run this command :
```sh
$ python manage.py createsuperuser # it will adding admin user creator, provide necessary data (username, email and password)
```
start server: 
```sh
$ python manage.py runserver 8080
```

Navigate to http://localhost:8080/admin and login with credits provided before
