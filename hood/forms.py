from django import forms
from .models import Profile, Neighbourhood


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']