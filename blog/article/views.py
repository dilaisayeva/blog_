from django.shortcuts import render
from .forms import *

# Create your views here.
def article(request):
    if request.method=='POST':
        f=articleAdd(request.POST)
        if f.is_valid():
            f.save()
    return render(request,'index.html',context={'article_add':articleAdd})
def home(request):
        return render(request,'home.html')
