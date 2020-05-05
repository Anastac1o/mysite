from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new


app_name = 'shop'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bootstrap', TemplateView.as_view(template_name='bootstrap/index.html')),
]


