from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def main(request):
    lists = Memo.objects.all()
    data = {'lists' : lists}
    
    return render(request, 'main.html', data)

def createMemo(request):
    memoContent = request.POST['memoContent']
    
    article = Memo(memo_text = memoContent)
    article.save()
    
    return HttpResponseRedirect(reverse('main'))

def writeMemo(request):
    if request.method == 'GET':
        return HttpResponse("to GET")
    if request.method == 'POST':
        return HttpResponse('to POST')

def modifyPage(request, idx):
    article = Memo.objects.get(id=idx)
    data = {'article': article}
    
    return render(request, 'modify.html', data)

def updateMemo(request):
    idx = request.POST['idx']
    memoContent = request.POST['memoContent']
    
    db_article = Memo.objects.get(id = idx)
    db_article.memo_text = memoContent
    db_article.save()
    
    return HttpResponseRedirect(reverse('main'))
    
def deleteMemo(request, idx):

    db_article = Memo.objects.get(id=idx)    
    db_article.delete()
    
    return HttpResponseRedirect(reverse('main'))