from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from django.template import loader
from .models import Item
from django.views.generic import CreateView


def index(request):
    return render(request, 'shop/index.html')

class CreateViewItem(CreateView):
    model = Item
    fields = ('name', 'author', 'is_rare', 'is_first_edition', 'is_used', 'is_new')
