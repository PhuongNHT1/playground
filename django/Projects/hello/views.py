from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    content = "<h1>Hello</h1> This is hello page"
    return HttpResponse(content)
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the HOME page")