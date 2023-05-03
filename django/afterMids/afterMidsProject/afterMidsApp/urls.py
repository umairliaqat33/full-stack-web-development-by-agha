from django.urls import path, include
from afterMidsApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
