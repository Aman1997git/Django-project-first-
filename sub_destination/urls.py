from django.urls import path
from . import views

urlpatterns = [

    path('India', views.india, name='india'),
    path('indonasia', views.indonasia, name='indonasia'),
    path('japan', views.japan, name='japan'),
    path('thailand', views.thailand, name='thailand'),
    path('nepal', views.nepal, name='nepal')

]