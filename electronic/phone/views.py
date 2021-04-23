from django.shortcuts import render,redirect
from .models import Phone
from .forms import PhoneForm
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    phone_data = Phone.objects.all
    return render(request, 'index.html', {'phone_data':phone_data})


def register(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/phone/index/')
    else:
        form = PhoneForm()
    return render(request, 'register.html', {'form': form})


def edit(request, id):
    phone_data = Phone.objects.get(id = id)
    form = PhoneForm(instance=phone_data)
    return render(request, 'update.html', {'form': form, 'id': id})


def update(request, id):
    phone_data = Phone.objects.get(id = id)
    form = PhoneForm(request.POST, instance=phone_data)
    if form.is_valid():
        form.save()
        return redirect('/phone/index/')
    return render(request, 'update.html', {'form': form})


def delete1(request, id):
    phone_data = Phone.objects.get(id = id)
    phone_data.delete()
    return redirect('/phone/index/')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('password')
        user = authenticate(username = uname, password = pwd)
        print(user)
        if user:
            return redirect('/phone/index/')
    return render(request, 'login.html', {})


def logout(request):
    # logout(request)
    return redirect('/phone/login/')

asdfghjkl;lkjhgfdsasdfghjkl;