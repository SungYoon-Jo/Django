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
        photo = request.FILES['images']

        board = Post(
            title=title,
            content=content,
            writer=writer,
            photo = photo,
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
        return render(request, 'root.html', context)
    
def createMemo(request):
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    photo = request.FILES['images']
    
    board = Post(
        title=title,
        content=content,
        writer=writer,
        photo = photo,
    )
    board.save()
    
    return HttpResponseRedirect(reverse('root'))

def main(request):
    
    lists = Post.objects.all()
    data = {'lists' : lists}

    print(data)
    return render(request, 'main.html', data)


def modifyPage(request, idx):
    
    article = Post.objects.get(id=idx)
    data = {'article': article}
    
    print(article)
    return render(request, 'modify.html', data)

def updatePage(request):
    idx = request.POST['idx']
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    images = request.POST['images']
    
    db_article = Post.objects.get(id = idx)
    
    db_article.title = title
    db_article.content = content
    db_article.writer = writer
    db_article.images = images
    
    db_article.save()
    
    return HttpResponseRedirect(reverse('root'))

def deletePage(request, idx):
    
    db_article = Post.objects.get(id=idx)    
    db_article.delete()
    
    return HttpResponseRedirect(reverse('root'))

def numPage(request, idx):
    
    article = Post.objects.get(id=idx)
    data = {'article': article}
    
    print(article)
    # return render(request, 'numPage', data)
    return render(request, 'root.html', data)


def upload(request):
    return render(request,'upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']
    except: 
        pass
    form.save()
    return redirect('/myprofile/profile/')  