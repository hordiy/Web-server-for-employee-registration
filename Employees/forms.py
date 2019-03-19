from django import forms
from .models import Profile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Фото')
    class Meta:
        model = Profile
        fields = ('avatar', )
