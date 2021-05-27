from django import forms
from .models import Hotel, Room, RoomType, Image
from user.models import User


class createHotel(forms.ModelForm):
    # manager_id = User.id
    class Meta:
        model = Hotel
        exclude = ['id']


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # fields = ('image',)
        # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        exclude=('room_type',)

class SearchRoom(forms.Form):
    Check_in = forms.DateInput()
