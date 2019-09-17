from django.shortcuts import render
from .forms import *

# Create your views here.
def comment(request):
    if request.method=='POST':
        f=commetAdd(request.POST)
        if f.is_valid():
            f.save()
    return render(request,'index3.html',context={'commentAdd':commetAdd})
