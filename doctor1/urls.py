from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('doctores', views.doctores,name='doctores'),
    path('doctores/crear', views.crear, name='crear'),
     path('doctores/editar', views.editar, name='editar'),
   
]