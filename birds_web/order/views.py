from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
#  about

def realtime(request):
    return render(request,'realtime.html')
#  about

def guide(request):
    return render(request,'guide.html')
#  about

def drOwl(request):
    return render(request,'drOwl.html')
#  about

def birdlist(request):
    return render(request,'birdlist.html')
#  about

def about(request):
    return render(request,'about.html')
#  about