from django.http import HttpRequest, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def nathan(request):
    return HttpResponse('Wassup Nathan')


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
