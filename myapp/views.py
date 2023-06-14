from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Nemovitost, Osoba

class NemovitostList(ListView):
    model = Nemovitost
    context_object_name = 'nemovitost_list'
    template_name = 'index.html'
class NemovitostDetailView(DetailView):
    model = Nemovitost
    context_object_name = 'nemovitost_detail'
    template_name = 'detailn.html'

class OsobaDetailView(DetailView):
    model = Osoba
    context_object_name = 'osoba_detail'
    template_name = 'detailn.html'
