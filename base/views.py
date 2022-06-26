from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>hw</h1>')


def room(request):
    return HttpResponse('<h1>room</h1>')
