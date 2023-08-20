# Create your tests here.
from apps.company.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index')
]

