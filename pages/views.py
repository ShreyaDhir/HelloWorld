from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000/sayHello

def myView(request) :
  return HttpResponse('Hello, World')
