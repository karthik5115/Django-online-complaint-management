from django import forms
from django.contrib.auth.models import User
from .models import UserInfo, Complaints


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('profile', )


class Raise_Complaint(forms.ModelForm):
    class Meta():
        model = Complaints
        fields = ('user', 'complaint_name', 'complaint_image',
                  'complaint_description', 'city', 'location', 'phone',)
