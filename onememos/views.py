from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *



def main(request):
    # return render(request, 'main.html')
    
    lists = Memo.objects.all()
    data = {'lists' : lists}
    
    return render(request, 'main.html', data)


def createMemo(request):
    # memoContent = request.POST['memoContent']
    
    # article = Memo(memo_text = memoContent)
    # article.save()
    
    # return HttpResponse('create memo = ' + memoContent)

    return HttpResponseRedirect(reverse('main'))

def writeMemo(request):
    # return HttpResponse('writeMemo good')
    
    if request.method == 'GET':
        return HttpResponse("to GET")
    if request.method == 'POST':
        return HttpResponse('to POST')