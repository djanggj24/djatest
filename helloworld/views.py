from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h3 >Hello World! Tried Again</h3>')




