from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def pp(request):
    return render(request,'pp.html')






