from django.urls import path
from . import views


urlpatterns = [
    path('',views.main, name='main'),
    path('createMemo/', views.createMemo),
    path('writeMemo/', views.writeMemo),
]