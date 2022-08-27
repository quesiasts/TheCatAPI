from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_breeds, name='index'),
    path('categories/<int:id>/', views.get_image_urls, name='get_image_urls')
]