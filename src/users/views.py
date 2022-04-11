from django.shortcuts import render, HttpResponse

# Create your views here.
def userIndex(request):
    return HttpResponse("Hello, world. You're at the Users index.")