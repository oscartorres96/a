from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the appointments index.")

def home(request):
    return render(request, "admin_panel/main.html")

def clients_dashboard(request):
    return render(request, "clients/main.html")