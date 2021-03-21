from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from models import user, notes

urlpatterns= [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=notes, template_name ="application/note.html"))
    
]