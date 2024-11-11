from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial
    path('new_post/', views.new_post, name='new_post'),
]