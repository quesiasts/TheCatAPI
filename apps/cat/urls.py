from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_breeds, name='index'),
    path('urls', views.get_image_urls, name='name-urls')
]