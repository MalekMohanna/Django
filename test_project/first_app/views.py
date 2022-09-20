from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("This is the equvilent of @app.route('/')")
