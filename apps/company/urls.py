from django.urls import path, include

from apps.company.views import *
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutViews.as_view(), name='about'),
    path('contact/', ContactViews.as_view(), name='contact'),
    path('team/', TeamViews.as_view(), name='team'),
    path('blog/', BlogViews.as_view(), name='blog'),

    path('blog/<int:id>',blog_detail),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
