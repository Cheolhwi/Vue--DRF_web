make sure you are at `Vue--DRF_web/djackets_django/`, first time to run the django back-end you should follow the command below.

```python
python manage.py makemigrations
python manage.py migrate
```

and use 

```python
python manage.py runserver
```

to start the back-end server
if you want to access the admin page, please use http://127.0.0.1:8000/admin/
and the superuser account is 
admin123
nmslcsb@123

make sure in file `Vue--DRF_web/djackets_django/djackets_django/settings.py`

make sure in the line 52 `http://localhost:8081 ` the port should be the same as the port in Vue.js front-end.

```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
]
```



