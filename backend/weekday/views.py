from rest_framework import generics

from .models import Weekday
from .serializers import WeekdaySerializer

class WeekDayDetailView(generics.RetrieveAPIView):
    queryset = Weekday.objects.all()
    serializer_class = WeekdaySerializer
    lookup_field = 'weekday'


class WeekDaylistView(generics.ListAPIView):
    queryset = Weekday.objects.all()
    serializer_class = WeekdaySerializer
