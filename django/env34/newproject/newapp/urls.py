
from django.urls import path
from newapp import views

urlpatterns = [
    path('agha', views.agha, name="agha"),
    path('', views.umair, name='umair'),
    path('umair', views.umair, name='umair'),

]
