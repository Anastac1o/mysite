from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'shop'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bootstrap', TemplateView.as_view(template_name='bootstrap/index.html')),
]