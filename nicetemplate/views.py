from django.shortcuts import render
from django.http import HttpResponse
from api.Utilities import Util

def index(request):
    return render(request, "nicetemplates/index.html")
