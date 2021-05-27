from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_view, name="booking"),
    path('payment', views.payment, name="payment"),
]