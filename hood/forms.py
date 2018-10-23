from django import forms
from .models import Profile, Neighbourhood, Business, Message


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']


class BizForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['user']