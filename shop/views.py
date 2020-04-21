from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Item
from django.views.generic import TemplateView, DetailView


def index(request):
    return render(request, 'shop/index.html', {"img":img})


class HomePageView(TemplateView):
    template_name = "bootstrap/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_items'] = Items.objects.all()
        return context

