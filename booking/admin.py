from django.apps import apps
from django.contrib import admin
from booking.models import Reservation, ReservationDetail


# for model in apps.get_app_config('booking').get_models():
#     admin.site.register(model)


class AdminReservation(admin.ModelAdmin):
    list_display = ('user', 'room_number', 'status', 'cost')


class AdminReservationDetail(admin.ModelAdmin):
    list_display = ('room_number', 'status')


admin.site.register(Reservation, AdminReservation)
admin.site.register(ReservationDetail, AdminReservationDetail)
