from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kompyuter

class KompListView(ListView):
    model = Kompyuter
    template_name = "komp/komp_list.html" 

class KompDetailView(DetailView):
    model = Kompyuter
    template_name = "komp/komp_detail.html"

