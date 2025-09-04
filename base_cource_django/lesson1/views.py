from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    context = {
        
    }
    return HttpResponse("Hello")