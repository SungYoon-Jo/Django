from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name='main'),
    path('root/', board, name='root'),
    
    
    # path('<str:idx>', numPage, name='numPage'),
    
    path('createMemo/', createMemo),
    path('root/modify/<str:idx>', modifyPage),
    path('root/modify/update/', updatePage),
    path('root/delete/<str:idx>', deletePage),
    
    # path('myprofile/upload/',myprofile.views.upload,name="upload"),    
    # path('myprofile/upload_create/',myprofile.views.upload_create,name="upload_create"),
    
  
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)