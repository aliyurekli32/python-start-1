from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('This is our new home...') 

# Create your views here.
