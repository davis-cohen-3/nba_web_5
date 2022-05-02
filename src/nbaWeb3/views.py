from curses.ascii import HT
from django.shortcuts import HttpResponse, render


# one view to just render main page for the localhost/8000
def index(request):
    #return render(request, 'home.html')
    return render(request, 'base.html')

