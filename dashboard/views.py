from django.shortcuts import render
from django.http import HttpResponse
from api.Utilities import Util


def index(request):
    return HttpResponse("Hello, world. You're at the appointments index.")

def home(request):
    return render(request, "admin_panel/main.html")

def clients_dashboard(request):
    return render(request, "clients/main.html")

def create_client(request):
    mimetype = "application/json"
    filters = Util().requestToJSON(request)
    return HttpResponse(dumps(Clients().create_client(filters)), mimetype)
