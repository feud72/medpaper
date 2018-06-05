from django.shortcuts import render
from django.views.generic import ListView

from .models import PubmedApi
# Create your views here.


class ApiListView(ListView):
    model = PubmedApi
    template_name = 'pubmed_api/pubmed_api_list.html'
