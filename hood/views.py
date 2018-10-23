from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import ProfileForm, HoodForm, BizForm, MessageForm
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from .models import Profile, Neighbourhood, Business, Message


@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    hood = Neighbourhood.objects.get(id=profile.neighbourhood.id)
    biz = Business.objects.filter(hood=hood.id)
    messages = Message.objects.filter(hood=hood.id)
    return render(request, 'index.html', {'hood': hood, 'biz': biz, 'profile': profile, 'user': user, 'messages': messages})


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


@login_required(login_url='/accounts/login')
def new_hood(request):
    user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.admin = user
            hood.save()
            return redirect('new_profile')
    else:
        hood_form = HoodForm()

    return render(request, 'new_hood.html', {'hood_form': hood_form})


@login_required(login_url='/accounts/login')
def new_biz(request):
    user = request.user
    if request.method == 'POST':
        biz_form = BizForm(request.POST)
        if biz_form.is_valid():
            biz = biz_form.save(commit=False)
            biz.user = user
            biz.save()
            return redirect('home')
    else:
        biz_form = BizForm()

    return render(request, 'new_biz.html', {'biz_form': biz_form})


@login_required(login_url='/accounts/login')
def new_message(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid():
            msg = msg_form.save(commit=False)
            msg.user = user
            msg.hood = profile.neighbourhood
            msg.save()
            return redirect('home')
    else:
        msg_form = MessageForm()

    return render(request, 'new_message.html', {'msg_form': msg_form})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/new_profile"


@login_required(login_url='accounts/login')
def business(request, id):
    business = Business.objects.get(id=id)
    return render(request, 'business.html', {'business': business})