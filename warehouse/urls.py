
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'add/', views.add, name='add'),
    url(r'move/', views.move, name='move'),
    url(r'^$', views.index, name='index'),
]