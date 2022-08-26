from django.contrib import admin

class BoardAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'content')

admin.site.register(Board, BoardAdmin)

