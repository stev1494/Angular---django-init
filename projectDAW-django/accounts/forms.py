from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Appointment

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length = 254, required = True, widget = forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostService(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['date','service','id_user']
