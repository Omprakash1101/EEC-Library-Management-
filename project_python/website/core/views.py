from django.shortcuts import render

from item.models import Category, Item, Books
# Create your views here.
def index(request):
    items = Books.objects.filter(is_sold=False)[:]
    categories = Category.objects.all()[:]
    return render(request,'core/index.html',{
        'categories': categories,
        'items' :items,
    })

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def policy(request):
    return render(request,'core/policy.html')

def terms(request):
    return render(request,'core/terms.html')

def sign(request):
    return render(request,'core/signup.html')