from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def mylogout(request):
    logout(request)
    return redirect('footballapp:home')

def mylogin(request):
    return render(request, 'loginform.html')
