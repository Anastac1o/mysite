

from .models import Item
from django.views.generic import TemplateView, DetailView


class HomePageView(TemplateView):
    template_name = "bootstrap/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_items'] = Item.objects.all()
        return context

