from django.shortcuts import render
from django.http import HttpResponse 
from .models import Student

# Create your views here.
#UrlConf Module. Every App has its own URL Config
def say_hello (request):
    obj = Student.objects.all()
    context={
        "obj" :  obj,
    }
#     This creates a dictionary called context.
# The key "obj" is used to store the obj QuerySet object.
# This context dictionary will be passed to the template when rendering it.
    return render(request, 'hello.html', context)