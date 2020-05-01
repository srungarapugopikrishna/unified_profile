# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .forms import InputUserProfileForm
from .models import UserProfile, Profile
from django.contrib.auth.models import User


def user_profile_input(request):
    if request.method == 'POST':
        form = InputUserProfileForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            facebook = form.cleaned_data['facebook']
            instagram = form.cleaned_data['instagram']
            twitter = form.cleaned_data['twitter']
            github = form.cleaned_data['github']
            stackoverflow = form.cleaned_data['stackoverflow']
            resume = form.cleaned_data['resume']
            hackerrank = form.cleaned_data['hackerrank']
            hackerearth = form.cleaned_data['hackerearth']
            others = form.cleaned_data['others']
            user = User.objects.get(username=request.user)
            user = Profile.objects.get(user_id=user.id)
            try:
                upo = UserProfile.objects.get(username_id=user.id)
            except Exception as e:
                upo = UserProfile()
            # upo.name = name
            upo.username = Profile.objects.get(user=request.user)
            print('Username:::', request.user)
            upo.email = email
            upo.facebook = facebook
            upo.instagram = instagram
            upo.twitter = twitter
            upo.github = github
            upo.stackoverflow = stackoverflow
            upo.resume = resume
            upo.hackerrank = hackerrank
            upo.hackerearth = hackerearth
            upo.others = others
            upo.save()
            try:
                user_profile = UserProfile.objects.get(username_id=user.id)
                user_profile_data = vars(user_profile)
                remove_items = ['_state', 'id', 'username_id']
                for item in remove_items:
                    user_profile_data.pop(item)
                user_profile_data['username'] = request.user
                return render(request, 'display_profile.html', {"data": user_profile_data})
            except Exception as e:
                return render(request, 'home.html')
    form = InputUserProfileForm()
    return render(request, 'input_user_profile.html', {'form': form, 'name': request.user})


def human_search(request):
    if request.method == 'POST':
        return render(request, 'home.html')
    return render(request, 'human_search_index.html')


def test(request):
    return render(request, 'human_search_index.html')


def user_profile_redirect(request, username, platform):
    try:
        user = User.objects.get(username=username)
        user = Profile.objects.get(user_id=user.id)
        user_profile = UserProfile.objects.get(username_id=user.id)
        user_profile_data = vars(user_profile)
        return HttpResponseRedirect(user_profile_data[platform])
    except Exception as e:
        return render(request, 'home.html')


def user_profile_display(request, username):
    try:
        user = User.objects.get(username=username)
        user = Profile.objects.get(user_id=user.id)
        user_profile = UserProfile.objects.get(username_id=user.id)
        user_profile_data = vars(user_profile)
        remove_items = ['_state', 'id', 'username_id']
        for item in remove_items:
            user_profile_data.pop(item)
        user_profile_data['username'] = request.user
        return render(request, 'display_profile.html', {"data": user_profile_data})
    except Exception as e:
        return render(request, 'home.html')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def home_new(request):
    if request.method == 'POST':
        form = InputUserProfileForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            facebook = form.cleaned_data['facebook']
            instagram = form.cleaned_data['instagram']
            twitter = form.cleaned_data['twitter']
            github = form.cleaned_data['github']
            stackoverflow = form.cleaned_data['stackoverflow']
            resume = form.cleaned_data['resume']
            hackerrank = form.cleaned_data['hackerrank']
            hackerearth = form.cleaned_data['hackerearth']
            others = form.cleaned_data['others']
            user = User.objects.get(username=request.user)
            user = Profile.objects.get(user_id=user.id)
            try:
                upo = UserProfile.objects.get(username_id=user.id)
            except Exception as e:
                upo = UserProfile()
            # upo.name = name
            upo.username = Profile.objects.get(user=request.user)
            print('Username:::', request.user)
            upo.email = email
            upo.facebook = facebook
            upo.instagram = instagram
            upo.twitter = twitter
            upo.github = github
            upo.stackoverflow = stackoverflow
            upo.resume = resume
            upo.hackerrank = hackerrank
            upo.hackerearth = hackerearth
            upo.others = others
            upo.save()
            try:
                user_profile = UserProfile.objects.get(username_id=user.id)
                user_profile_data = vars(user_profile)
                remove_items = ['_state', 'id', 'username_id']
                for item in remove_items:
                    user_profile_data.pop(item)
                user_profile_data['username'] = request.user
                return render(request, 'home_new.html',
                              {'form': form, 'name': request.user, "user_data": user_profile_data})
                # return render(request, 'display_profile.html', {"data": user_profile_data})
            except Exception as e:
                return render(request, 'home.html')
    form = InputUserProfileForm()
    user = User.objects.get(username=request.user)
    user = Profile.objects.get(user_id=user.id)
    user_profile = UserProfile.objects.get(username_id=user.id)
    print(vars(user_profile))
    user_profile_data = vars(user_profile)
    remove_items = ['_state', 'id', 'username_id', 'name']
    for item in remove_items:
        user_profile_data.pop(item)
    print(vars(user_profile))
    user_profile_data['username'] = request.user
    return render(request, 'home_new.html', {'form': form, 'name': request.user, "user_data": user_profile_data})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})