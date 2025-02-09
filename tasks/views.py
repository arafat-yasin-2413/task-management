from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is home")

def contact(request):
    return HttpResponse("this is contact")

def show_task(request):
    return HttpResponse("this is show task")



    