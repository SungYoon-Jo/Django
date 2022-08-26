from django.forms import ModelForm
from .models import *


class BoardForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'writer']