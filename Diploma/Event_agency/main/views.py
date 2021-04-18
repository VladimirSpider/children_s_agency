from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse ("<h4>Hello</h4>")
    return render(request, 'main/index.html')

def about_us(request):
    #return HttpResponse ("<h4>about_us</h4>")
    return render(request, 'main/about_us.html')