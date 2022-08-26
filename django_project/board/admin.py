import imp
from django.contrib import admin
from board.models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'content')

admin.site.register(Board, BoardAdmin)

