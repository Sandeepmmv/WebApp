from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class SignUpForm(UserCreationForm):
    # fname = forms.CharField(label='Enter First Name :',max_length=100)
    # lname = forms.CharField(label='Enter Last Name :',max_length=100)
    # email = forms.EmailField(label='Email-Id :')
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profileimage','bio','location','birth_date']