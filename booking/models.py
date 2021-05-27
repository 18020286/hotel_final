from django.db import models
from hotel.models import *
from user.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    cost = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='room_number')
    trading_code = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    RESERVATION_STATUS = (
        ('confirmed', 'Confirmed'),
        ('checkedin', 'Checked in'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=RESERVATION_STATUS, max_length=12, default='pending')

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return '%s book %s' % (self.user.username, self.room_number.room_type)

    
class ReservationDetail(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='room_number')
    reserved = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ROOM_STATUS = (
        ('checked in', 'Checked in'),
        ('checked out', 'Checked out'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=ROOM_STATUS, max_length=11)

    class Meta:
        db_table = 'reservation_detail'
        unique_together = ('room_number', 'reserved')


class Review(models.Model):
    reserv = models.OneToOneField(Reservation, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=1)
    comment = models.CharField(max_length=500, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        db_table = 'review'
