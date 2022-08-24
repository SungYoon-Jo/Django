from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main(request):
    # return HttpResponse("Onememos~ Hello, World~ ")
    return render(request, 'main.html')

def createMemo(request):

    memoContent = request.GET['memoConten']
   
    print(memoContent)     
    
    return HttpResponse('hi Create memo = ' + memoContent)
