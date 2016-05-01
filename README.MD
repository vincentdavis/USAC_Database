A RESTful API written in Django for lookup USAC race results


## Setting up
This project was built with python +3.5

```bash
$ virtualenv -p python3 env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ cd usacdata
$ python manage.py migrate --settings=coprop.settings_development
$ python manage.py runserver  --settings=coprop.settings_development
```

Then head to http://localhost:8000/api/v1/ in your browser to get started.

username: admin
password: test1234