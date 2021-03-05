from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.forms import ModelForm
from django.forms.widgets import *

class ProfileModelForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'bio', 'image')


class RegisterForm(ModelForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=PasswordInput)
	email = forms.CharField(widget=EmailInput)
	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	ip_address = forms.GenericIPAddressField()
	mac_address = forms.CharField(max_length=100)