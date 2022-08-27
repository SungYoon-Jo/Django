from django.urls import path
from .views import *

urlpatterns = [
    # path('', board, name='board'),
    path('', tp, name='tp'),
    path('createMemo/', createMemo),
]