from django import forms
from django.conf import settings

from .models import UserProfile

class LoginForm(forms.Form):
	email_attrs = {'class':'form-control', 'placeholder':'Email Address'}
	email = forms.CharField(label='Email Address', widget=forms.EmailInput(attrs=email_attrs))		
	password_attrs = {'class':'form-control', 'placeholder':'Password'}
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs=password_attrs))
	
class RegisterForm(forms.Form):
	email_attrs = {'class':'form-control', 'placeholder':'Email Address'}
	email = forms.CharField(label='Email Address', widget=forms.EmailInput(attrs=email_attrs))		
	password_attrs = {'class':'form-control', 'placeholder':'Password'}
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs=password_attrs))
	password_again_attrs = {'class':'form-control', 'placeholder':'Password Confirm'}
	password_again = forms.CharField(label='Password Match',widget=forms.PasswordInput(attrs=password_again_attrs))
	
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['first_name', 'last_name']
		widgets = {
    	'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
    }