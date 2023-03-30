from django.conf.urls import url
from . import views
from django.urls import path

app_name = "admin_center"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin_panel/', views.home, name="home"),

    path('admin_panel/clients', views.clients_dashboard, name="clients_dashboard"),
    path('admin_panel/createClient', views.create_client, name='create_client'),
]