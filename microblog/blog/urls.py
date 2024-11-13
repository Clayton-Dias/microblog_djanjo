from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial
    path('new_post/', views.new_post, name='new_post'), # Página da nova postagem
    path('about/', views.about, name='about'), # Página Sobre
    path('sucess/', views.success, name='success')
]