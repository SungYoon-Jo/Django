from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("Onememos~ Hello, World~ ")

def createMemo(request):

    request.GET['somekey']

    return HttpResponse('')
