from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        board = Post(
            title=title,
            content=content,
            writer=writer,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Post.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'frist.html', context)
    
def createMemo(request):
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    
    board = Post(
        title=title,
        content=content,
        writer=writer,
    )
    board.save()
    
    return HttpResponseRedirect(reverse('main'))

def main(request):
    
    return render(request, 'main.html')

def modifyPage(request, idx):
    
    article = Post.objects.get(id=idx)
    data = {'article': article}
    
    print(article)
    return render(request, 'modify.html', data)

def updatePage(request):
    idx = request.POST['idx']
    memoContent = request.POST['memoContent']
    
    db_article = Post.objects.get(id = idx)
    
    db_article.title = memoContent
    db_article.content = memoContent
    db_article.writer = memoContent
    
    db_article.save()
    
    return HttpResponseRedirect(reverse('frist'))

def deletePage(request):
    return HttpResponse('deletePage')

