from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.index, name='create_hotel'),
    path('about-us/', views.about_us_view, name='about-us'),
]
