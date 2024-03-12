from django.shortcuts import render
from django.http import HttpResponse

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):    
    return HttpResponse("hello")
def pages(request):
    pass