from django.urls import path
from AppMedica import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),

    ]