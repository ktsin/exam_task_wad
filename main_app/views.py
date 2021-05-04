from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from main_app.forms import AuthorizeForm, RegisterForm
from main_app.models import SystemUser


def layout_example(request):
    return render(request, 'layout.html')


# USER MANIPULATIONS


def auth_user(request):
    if not request.user.is_anonymous:
        return redirect('/profile/')
    if request.method == "GET":
        form = AuthorizeForm()
        return render(request, 'users/login.html', {"form": form, 'title': 'Вход'})
    else:
        data = {'name': request.POST.get("username"),
                'password': request.POST.get("password")}
        if not SystemUser.objects.filter(username=data['name']).exists():
            form = AuthorizeForm(request.POST)
            form.add_error('username', 'Пользователя с данным именем не существует')
            return render(request, 'users/login.html', {'form': form, 'title': 'Ошибка входа'})
        else:
            user = authenticate(request, username=data['name'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                form = AuthorizeForm(request.POST)
                form.errors['username'] = ""
                form.add_error('password', 'Неправильный пароль')
                return render(request, 'users/login.html', {'form': form})


def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'users/register.html', {"form": form, 'title': 'Регистрация'})
    else:
        data = {
            'email': request.POST.get("email"),
            'name': request.POST.get("username"),
            'password': request.POST.get("password")}
        if SystemUser.objects.filter(username=data['name']).exists():
            form = RegisterForm(request.POST)
            form.add_error('username', 'Пользователь с данным логином уже существует')
            return render(request, 'users/register.html', {'form': form, 'title': 'Регистрация'})
        else:
            user = SystemUser.objects.create_user(data['name'], data['password'])
            login(request, user)
            return redirect('/profile/')


def profile(request):
    usrn = request.user.username
    user = SystemUser.objects.get(username=usrn)
    return render(request, 'users/profile.html', {'title': 'Your profile', 'user': user})