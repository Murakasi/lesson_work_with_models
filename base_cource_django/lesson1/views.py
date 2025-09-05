from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from lesson1.forms import ReportForm
# Create your views here.

def index(request: HttpRequest, name):
    name_user = name
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    elif request.method == "GET":
        form = ReportForm()
    context = {
        "name": name_user,
        "form": form,
    }
    return render(request, "lesson1/index.html", context)