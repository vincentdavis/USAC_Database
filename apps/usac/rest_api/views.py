from rest_framework import viewsets

from .serializers import *
from apps.usac.models import *

# from .filters import PropertyFilter

__all__ = (
    "DirectorView",
    "PromoterView",
    "EventTypeView",
    "EventDayView",
    "RaceView",
    "ParticipantView",
    "EventView",
    "RaceResultView",
    "LapTimesView",
)


class DirectorView(viewsets.ModelViewSet):
    """ rest api Director resource. """

    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_fields = ('name',)
    ordering_fields = '__all__'


class PromoterView(viewsets.ModelViewSet):
    """ rest api Promoter resource. """

    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    filter_fields = ('name',)
    ordering_fields = '__all__'


class EventTypeView(viewsets.ModelViewSet):
    """ rest api EventType resource. """

    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    filter_fields = ('name',)
    ordering_fields = '__all__'


class EventDayView(viewsets.ModelViewSet):
    """ rest api EventDay resource. """

    queryset = EventDay.objects.all()
    serializer_class = EventDaySerializer
    filter_fields = ('event', 'search_id', 'day', 'url', 'multi_page')
    ordering_fields = '__all__'


class RaceView(viewsets.ModelViewSet):
    """ rest api Race resource. """

    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_fields = ('event_day', 'name', 'race_id', 'url')
    ordering_fields = '__all__'


class RaceResultView(viewsets.ModelViewSet):
    """ rest api RaceResult resource. Place, Points, Name, City, State, Time, USAC#, Bib, Team"""

    queryset = RaceResult.objects.all()
    serializer_class = RaceResultSerializer
    filter_fields = ('race', 'place', 'points', 'participant', 'city_state', 'result_time', 'usac', 'bib', 'team')
    ordering_fields = '__all__'

class LapTimesView(viewsets.ModelViewSet):
    """ LapTimes RaceResult, Lap1, Lap2, Lap3, Lap4"""

    queryset = LapTimes.objects.all()
    serializer_class = LapTimesSerializer
    filter_fields = ('result', 'lap1', 'lap2', 'lap3', 'lap4')
    ordering_fields = '__all__'


class ParticipantView(viewsets.ModelViewSet):
    """ rest api Participant resource. """

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_fields = ('lname', 'fname', 'address', 'license')
    ordering_fields = '__all__'


class EventView(viewsets.ModelViewSet):
    """ rest api Event resource. """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = (
        'name', 'location', 'state', 'start_date', 'end_date',
        'flyer_url', 'website_url', 'online_reg',
        'permit_number', 'director', 'promoter',
    )
    ordering_fields = '__all__'
