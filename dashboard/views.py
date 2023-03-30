from django.shortcuts import render
from django.http import HttpResponse
from api.Utilities import Util
from bson.json_util import loads, dumps
from dashboard.Clients import Clients
import json



def index(request):
    return HttpResponse("Hello, world. You're at the appointments index.")

def home(request):
    return render(request, "admin_panel/main.html")

def clients_dashboard(request):
    return render(request, "clients/main.html")

def create_client(request):
    mimetype = "application/json"
    data = json.loads(request.body)
    return HttpResponse(dumps(Clients().create_client(data)), mimetype)
