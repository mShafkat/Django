from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django(request):
    return HttpResponse("Django is awesome")
