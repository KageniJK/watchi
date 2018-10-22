from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from .models import Profile


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login')
def profile_setup(request):
    user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST)
        if prof_form.is_valid():
            profile = Profile.objects.get(user=user)
            profile.bio = prof_form.cleaned_data['bio']
            profile.location = prof_form.cleaned_data['location']
            profile.neighbourhood = prof_form.cleaned_data['neighbourhood']
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        prof_form = ProfileForm()

    return render(request, 'registration/profile_form.html', {'prof_form': prof_form})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/new_profile"
