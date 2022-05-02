from curses.ascii import HT
from django.shortcuts import HttpResponse, render

def index(request):
    #return render(request, 'home.html')
    return render(request, 'base.html')

