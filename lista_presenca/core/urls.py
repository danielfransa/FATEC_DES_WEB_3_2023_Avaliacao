from django.urls import path
from . import views

urlpatterns = [
  path('', views.cadastro, name='cadastro'),
  path('lista', views.listar, name='lista'),
]
