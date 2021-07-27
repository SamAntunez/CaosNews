from django.contrib import admin
from django.urls import path,include
from .views import caos,galeria,formulario,registro

urlpatterns = [
    path('',caos,name='CAOS'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('registro/', registro,name='REG'),
]