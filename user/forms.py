from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# class RegistrationForm(forms.Form):
#     username = forms.CharField(label="username", max_length=150)
#     password1 = forms.CharField(label="password", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="re-password", widget=forms.PasswordInput)
#
#     def clean_password2(self):
#         if 'password1' in self.cleaned_data:
#             password1 = self.cleaned_data['password1']
#             password2 = self.cleaned_data['password2']
#             if password1 == password2 and password1:
#                 return password2
#         raise forms.ValidationError("password is not match.")
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not re.search(r'^\w+$', username):
#             forms.ValidationError("username contain special characters.")
#         try:
#             User.objects.get(username=username)
#         except ObjectDoesNotExist:
#             return username
#         raise forms.ValidationError("username already exits.")
#
#     def save(self):
#         User.objects.create(username=self.cleaned_data['username'], password=self.cleaned_data['password2'])


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')
        # fields = '__all__'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'dob', 'phone', 'email')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'dob')


class StaffCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'dob', 'is_staff')
