from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from demoapp.models import employee

# Create your views here.
def display(request):
    n={"name":"nawas"}


    return render(request,'demo.html',n)
