from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest, name):
    name_user = name
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    context = {
        "name": name_user,
    }
    return render(request, "lesson1/index.html", context)