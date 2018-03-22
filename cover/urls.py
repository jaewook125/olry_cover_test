from django.urls import path
from . import views

app_name = 'cover'

urlpatterns = [
	path('', views.index, name='index'),
	path('image.jpg', views.image_generater, name='image_generater'),
]