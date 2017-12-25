[![Code Issues](https://www.quantifiedcode.com/api/v1/project/da548768516a41a29c2f7b38448c14d9/badge.svg)](https://www.quantifiedcode.com/app/project/da548768516a41a29c2f7b38448c14d9)

A RESTful API written in Django for lookup USAC race results


## Setting up
This project was built with python +3.5

```bash
$ virtualenv -p python3 env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ cd usacdata
$ python manage.py migrate --settings=usacdata.settings.local
$ python manage.py runserver  --settings=usacdata.settings.local
```

Then head to http://localhost:8000/api/v1/ in your browser to get started.

username: admin
password: test1234
