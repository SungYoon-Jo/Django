from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('frist/', board, name='frist'),
    path('createMemo/', createMemo),
    path('frist/modify/<str:idx>', modifyPage),
    path('frist/modify/update/', updatePage),
    path('delete/<str:idx>', deletePage),
]