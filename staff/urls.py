from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('blog/', views.blog_management_view, name="admin-blog"),
    path('add-blog/', views.NewPost, name="add_blog"),
    path('edit-blog/<int:id>', views.EditPost, name="edit_blog"),

    path('room/', views.room_view, name="admin-room"),
    path('room/add', views.AddRoom, name="add_room"),
    # path('edit-blog/<int:id>', views.EditPost, name="edit_blog"),

    path('account/', views.ViewAccount, name="admin-account"),
    path('account/add', views.RegisterAcc, name="admin-regis"),
    path('account/<int:id>/<str:action>', views.ChangeAccStatus, name="admin-action"),

    path('reservation_management', views.reservation_management_view, name="reservation_management"),
    path('room_category', views.room_category_view, name="room_category"),
    path('room_category/edit/<str:type>', views.edit_category_view, name="edit_category"),
    path('room_category/add', views.New_Room_Type, name="add_category"),



]
# urlpatterns = [
#     path('', views.CustomerProfileView, name='profile'),
# ]