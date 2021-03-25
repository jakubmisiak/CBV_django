from django.views.generic.list import ListView
from Backend.models.restaurant import Restaurant
from django.core.paginator import Paginator
from django.shortcuts import render


class HomeView(ListView):
    model = Restaurant
    template_name='home.html'
    context_object_name='restaurant_list'
    paginate_by=10
    ordering = ['-id']

