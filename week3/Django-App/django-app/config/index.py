from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request, 'home.html')

def catering(request):
    return render (request, 'catering.html')

def menu(request):
    return render (request, 'menu.html')

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')