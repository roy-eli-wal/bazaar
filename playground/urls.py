from django.urls import path
from . import views

#  map our urls to our view functions
urlpatterns = [
    path('hello/', views.say_hello)
]