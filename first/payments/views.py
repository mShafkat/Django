from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse("Django is cool!")

def bkash(request):
    return HttpResponse("This is bkash payment gateway.")

def add(request):
    z = 30+34
    return HttpResponse(f"The sum is {z}")

def format(request):
    name = "Kat"
    version = "unknown"
    return HttpResponse(f"This is {name} version {version}")