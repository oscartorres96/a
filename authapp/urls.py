from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.login_view, name='login_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]