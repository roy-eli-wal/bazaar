from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .reg_forms import RegisterationForm

from item.models import Category, Item 
def index(request):
    return render(request,'core/index.html')


def contact(request):
    return render(request, 'core/contact.html')
def about(request):
    return render(request,'core/about.html')
def termofuse(request):
    return render(request,'core/termsofuse.html')   
def privacypolicy(request):
    return render(request,'core/privacypolicy.html')
def items(request):
    items = Item.objects.filter(listing_is_sold = False)[0:8]
    categories = Category.objects.all()
    return render(request, 'core/list_items.html', {
        "categories": categories,
        "items" : items
    })

def userRegisterion(request):
    # reg_form = RegisterationForm()
    if request.method == 'POST':
        reg_form = RegisterationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/signin/')
    else:
        reg_form = RegisterationForm()    

    return render(request, 'core/user_reg_form.html', {
        'reg_form' : reg_form
    })
def user_logout(request):
    logout(request)
    return redirect('index')

