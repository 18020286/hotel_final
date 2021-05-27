import django_filters
from hotel.models import *


class RoomFilter(django_filters.FilterSet):
    room_number = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Room
        # fields = '__all__'
        fields = ['room_number', 'room_type__room_type', 'status', 'room_type__num_person']

    def __init__(self, *args, **kwargs):
        super(RoomFilter, self).__init__(*args, **kwargs)
        self.filters['room_type__num_person'].label = "Capacity"
        self.filters['room_type__room_type'].label = "Room type"
