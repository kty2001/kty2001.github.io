from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(type(request))
    print(request)
    return HttpResponse('Hello django')

def helloworld(request):
    return HttpResponse('Hello World!')

def home(request):
    return render(request, 'first/home.html')