# grupo-2-backend



## Creating your venv environment (Running localy)
```
python3 -v venv .venv
```
to activate 
```
source .env/bin/activate
```
To deactivate
```
deactivate
```

### install packages 
pip install requirements.txt

### Running inside Docker container
first, build the image
```
docker build .
```
then run the image that was builded 
```
docker-compose up
```
go to http://localhost:8000/

Mongodb will be running on mongodb://root:root@localhost:27017/
### running Django
```
python manage.py migrate
python manage.py runserver
```