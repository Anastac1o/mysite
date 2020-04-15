from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from django.template import loader

def index(request):
    template = loader.get_template('shop/index.html')
    return HttpResponse("Shop")