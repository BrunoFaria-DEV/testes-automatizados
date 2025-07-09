from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('criar/', views.criar_pessoa, name='criar_pessoa'),
    path('editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
]