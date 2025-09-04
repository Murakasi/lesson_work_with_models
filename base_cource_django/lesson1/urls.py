from django.urls import path
from lesson1 import views

urlpatterns = [
    path("home/<str:name>/", views.index, name="index"),
]
