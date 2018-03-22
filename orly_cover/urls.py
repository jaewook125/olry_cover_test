
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover/', include('cover.urls', namespace='cover')),
    path('', lambda r: redirect('cover:index')),
    #루트주소로 이동시키는 코드 cover/index로
]
