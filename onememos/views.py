from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main(request):
    return render(request, 'main.html')

def createMemo(request):
    memoContent = request.POST['memoContent']
    
    article = Memo(memo_text = memoContent)
    article.save()
    
    return HttpResponse('create memo = ' + memoContent)

    