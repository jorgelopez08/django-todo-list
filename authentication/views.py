from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .forms import UserForm, LoginForm
# Create your views here.


def login(request):
    if request.session.get('auth_user'):
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
            except ObjectDoesNotExist:
                return render(request, 'login.html', {'alert': 'User not found'}, status=404)

            if not check_password(form.cleaned_data['password'], user.password):
                return render(request, 'login.html', {'alert': 'Incorrect password'}, status=401)
            # Todo: change user.id for JWT
            request.session['auth_user'] = user.id
            return redirect('/')
    return render(request, 'login.html', {'user': None})


def register(request):
    # Todo: change user.id for JWT
    if request.session.get('auth_user'):
        return redirect('/')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = {
                'email': form.cleaned_data['email'],
                'username': form.cleaned_data['username'],
                'password': form.cleaned_data['password'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
            }
            new_user = User.objects.create_user(**data)
            new_user.is_staff = False
            new_user.save()
        return redirect('/login/')
    return render(request, 'register.html', {'user': None})


# Implement logout method
def logout(request):
    try:
        del request.session['auth_user']
        HttpResponse().delete_cookie('sessionid')
    except KeyError:
        print('Session not deleted')
    return redirect('/login')
