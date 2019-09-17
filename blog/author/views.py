from django.shortcuts import render
from .forms import authorAdd
# Create your views here.
def author(request):
    if request.method=='POST':
        f=authorAdd(request.POST)
        if f.is_valid():
            f.save()
    return render(request,'index1.html',context={'author_add':authorAdd})
