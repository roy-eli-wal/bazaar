from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
#UrlConf Module. Every App has its own URL Config
def say_hello (request):
    return render(request, 'hello.html')