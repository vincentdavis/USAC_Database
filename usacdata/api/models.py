from django.db import models
from datetime import datetime

class Event(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    location = models.CharField(max_length=255, null=False, unique=False)
    # TODO: Should state have its own class
    state = models.CharField(max_length=2, null=False, unique=False)
    dates = models.CharField(max_length=255, null=False, unique=False)
    # TODO: calculate start and end from dates, see start_end function below
    startdate = models.DateField(null=False, unique=False) #created from dates
    enddate = models.DateField(null=False, unique=False) #created from dates, same as start date is 1 day
    flyer_url = models.URLField(max_length=255, null=True)
    flyer = models.FileField(upload_to='uploads/flyers/')
    website_url = models.URLField(max_length=255, null=True)
    online_reg = models.URLField(max_length=255, null=True)
    # TODO: is permit number unique? I am assuming yes.
    permitnum = models.CharField(max_length=255, null=False, unique=True) # not sure if this is unique
    # promoter = models.CharField(max_length=255, null=False, unique=False)
    # director = models.CharField(max_length=255, null=False, unique=False)

    def start_end(self):
        """
        Convert date to sart and end date.
        If one date then bofth start and end are the same.
        example value "04/22/2010 - 04/25/2010"
        """
        d = self.date.strip().split(' - ')
        self.startdate = d[0]
        try:
            self.enddate = d[1]
        except IndexError:
            self.enddate = d[0]

class Director(models.Model):
    """
    Person Directing the Event
    Many Events for each Director
    """
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255, null=False, unique=True)


class Promoter(models.Model):
    """
    Company promoting the Event
    Many Event promoted by Each company
    """
    event = models.ForeignKey(Event) # many event to 1 Director
    name = models.CharField(max_length=255, null=False, unique=True)

class EventType(models.Model):
    """
    Each event has an event type. This is not well defined
    This is many to many with event
    Each even has many types and each type is part of many events
    """
    event = models.ManyToManyField(Event)
    etype = models.CharField(max_length=255, null=False, unique=False)

class EventDay(models.Model):
    """
    Each day or races is part of an event.
    Each race is part of a day, see rece below.
    The day has an id on the website, 44746 in the example below, Also a date 01/15/2012.
    Not all days have an searchid or a page, sometimes all the results are on 1 page.
    <a href="javascript:void(0)" onclick="loadInfoID(44746,'Criterium 01/15/2012')">Criterium</a>

    Multiple day example
    https://www.usacycling.org/results/?permit=2012-860
    This is the rusults for the second race of the first day.
    https://www.usacycling.org/results/index.php?ajax=1&act=loadresults&race_id=598962
    """
    event = models.ForeignKey(Event)
    searchid =  models.IntegerField(default=None, null=True)
    day = models.DateField(null=False, unique=False)
    url = models.URLField(max_length=255, null=False) # https://www.usacycling.org/results/?permit=2012-860
    # TODO Maybe need a switch for single page or multi page. Trying this below.
    multipage = models.BooleanField()

class Race(models.Model):
    """
    Each race and results
    """
    event = models.ForeignKey(Event, null=True)
    eventday = models.ForeignKey(EventDay, null=True)
    name = models.CharField(max_length=255, null=False) # this is often a class or race category
    race_id = models.IntegerField(default=None, null=False)
    url = models.URLField(max_length=255, null=False) # "https://www.usacycling.org/results/index.php?ajax=1&act=loadresults&race_id=598962"

class Participant(models.Model):
    """
    Racers
    """
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    license = models.CharField(max_length=255, null=False)

# TODO RaceResults class





