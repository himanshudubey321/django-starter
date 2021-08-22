from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # print("HELLO 1123")
    # context = {
    #     "name": "hello world",
    #     "age": 22121
    # }
    # return render(request, 'index.html', context)
    return HttpResponse("Hello, world. You're at the polls index.512")


def home(request):
    return HttpResponse("Home ")
