from django.shortcuts import render, redirect


def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, 'django_app/home.html', context=data)
