from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 


def home(request):
    return render (request,'selling/home.html')

def about(request):
    return render (request,'selling/about.html')

def apple(request):
    return render (request,'selling/apple.html')    


def sign_up(request):
    return render (request,'selling/sign_up.html')

def mobile_brand(request):
    return render (request,'selling/mobile_brand.html')

def get_paid(request):
    return render (request,'selling/get_paid.html')

def evaluation(request):
    return render (request,'selling/evaluation.html')

def customer(request):
    return render (request,'selling/customer.html')

def google(request):
    return render (request,'selling/google.html')

def mobile_no(request):
    return render (request,'selling/mobile_no.html')


def motorola(request):
    return render (request,'selling/motorola.html')

def nokia(request):
    return render (request,'selling/nokia.html')

def oneplus(request):
    return render (request,'selling/oneplus.html')


def realme(request):
    return render (request,'selling/realme.html')

def samsung(request):
    return render (request,'selling/samsung.html')

def vivo(request):
    return render (request,'selling/vivo.html')


def xioami(request):
    return render (request,'selling/xioami.html')






