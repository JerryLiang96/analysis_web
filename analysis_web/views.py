from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from comment import models
from .forms import LoginForm, RegForm, BindEmailForm


def home(request):
    context = {}
    object_list = models.Movie.objects.filter(is_show=True).values(
        'id',
        'name',
        'poster',
        'score',
    )
    movie_list = []
    for item in object_list:
        item['poster'] = item['poster'].replace('\\', '/').replace(
            'C:/Users/lzr/analysis_web', '')
        movie_list.append(item)
    context['movie_list'] = movie_list
    return render(request, 'home.html', context)


def web_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def web_register(request):
    if request.method == "POST":
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


def web_logout(request):
    logout(request)
    return redirect(request.GET.get('from', reverse('home')))


@login_required
def user_info(request):
    context = {}
    return render(request, 'user_info.html', context)
