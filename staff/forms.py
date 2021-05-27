from django import forms
import re
from blog.models import *
from hotel.models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms import FileField
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password','is_superuser')
        # fields = ('first_name', 'last_name', 'dob', 'phone' , 'email', 'is_staff')

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = '__all__'


# class CategoryForm(forms.ModelForm):

#     class Meta:
