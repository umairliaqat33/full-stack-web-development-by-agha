from django.urls import path
from impactApp import views


urlpatterns = [
    path('', views.index, name='index')
]
