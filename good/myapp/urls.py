from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('root/', board, name='root'),
    
    path('<str:idx>', numPage, name='numPage'),
    
    path('createMemo/', createMemo),
    path('root/modify/<str:idx>', modifyPage),
    path('root/modify/update/', updatePage),
    path('root/delete/<str:idx>', deletePage),
]