from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('register/', views.SiteRegisterView.as_view(), name="register"),
    path('register_ok/', views.SiteRegisterOkView.as_view(), name="register_ok"),
    path('', views.index, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.edit_profile, name='profile'),
    path('admin-page/', views.view_admin_page, name='admin-page')

]
