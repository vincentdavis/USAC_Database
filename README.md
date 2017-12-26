[![Code Issues](https://www.quantifiedcode.com/api/v1/project/da548768516a41a29c2f7b38448c14d9/badge.svg)](https://www.quantifiedcode.com/app/project/da548768516a41a29c2f7b38448c14d9)

A RESTful API written in Django for lookup USAC race results


## Setting up
This project was built with python +3.5

```bash
$ virtualenv -p python3 env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ cd usacdata
$ python manage.py migrate --settings=usacdata.settings_development
$ python manage.py runserver  --settings=usacdata.settings_development
```

Then head to http://localhost:8000/api/v1/ in your browser to get started.

username: admin
password: test1234

#Settings
##Create environment file using **.env_template** file in root directory
    
    $ cp .env_template .env


#AWS

##Update pip
###If you’re using Python 2 run:

	$ sudo pip install --upgrade pip

###For Python 3:

	$ sudo pip3 install --upgrade pip

##Install Elastic Beanstalk CLI
###For Python 2:

	$ pip install --upgrade --user awsebcli

###For Python 3:

	$ pip3 install --upgrade --user awsebcli

##Adding to path
###Add the following line at the end of ~/.profile

	$ export PATH=~/.local/bin:$PATH


##EB CLI
###Initialize elastic beanstalk

    $ eb init
    
###To create a new app you should type

    $ eb create
    
###After every change commit files using git
###Then deploy

    $ eb deploy
    
###Once it's finished you will be able to open it

    $ eb open