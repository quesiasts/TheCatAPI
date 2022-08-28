from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_breeds, name='index'),
    path('images/:id/', views.get_image_urls, name='get_image_urls')
]