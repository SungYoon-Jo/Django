from turtle import title
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
    
    return HttpResponseRedirect(reverse('board'))