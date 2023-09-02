from django.urls import path
from . import views

urlpatterns = [
    path('nicetemplate/', views.index, name='index'),
]