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

## Docker:

### Project is configured to run in docker enviroment 

Please ensure that you have docker installed on your system (https://docs.docker.com/engine/installation/)

To run example in docker enviroment follow this steps:
- Download repository
```sh
git clone https://github.com/TRaffii/DjangoSimpleExampleProject.git
```
- Go to project directory 
```sh
cd DjangoSimpleExampleProject
```
- Change chmod of docker-entrypoint.sh file 
```sh
chmod u+x docker-entrypoint.sh
```
- Build docker image
```sh
sudo docker build -t <youruser>/mentor_candidate:latest . 
```
Where <youruser> is you unique username
- Run image 
```sh
sudo docker run --publish=<yourip>:8080:8080 <youruser>/mentor_candidate   
```
Where yourip is our computer ip for example 192.168.0.10

Then you should be able to login in http://192.168.0.10/admin with below credits:
- user: admin
- password: password12345

