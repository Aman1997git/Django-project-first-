from django.shortcuts import render
from .models import *

# Create your views here.


def india(request):

    india_des = IndiaDestionation.objects.all()
    return render(request, 'india.html', {'india_des': india_des})


def nepal(request):
    nepal_des = NepalDestionation.objects.all()
    return render(request, 'nepal.html', {'nepal_des': nepal_des})

def indonasia(request):
    indo_des = IndonasiaDestionation.objects.all()
    return render(request, 'indonasia.html', {'indo_des': indo_des})


def japan(request):
    japan_des = JapanDestionation.objects.all()
    return render(request, 'japan.html', {'japan_des': japan_des})


def thailand(request):
    thai_des = ThailandDestionation.objects.all()
    return render(request, 'thailand.html', {'thai_des': thai_des})