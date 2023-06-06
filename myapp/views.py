from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Nemovitost


class BytListView(ListView):
    model = Nemovitost
    context_object_name = 'byty_list'
    template_name = 'index.html'


class BytDetailView(DetailView):
    model = Nemovitost
    context_object_name = 'byt_detail'
    template_name = 'byt.html'
