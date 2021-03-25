from django.views.generic import CreateView
from Backend.forms.restaurant_form import RestaurantForm
from django.shortcuts import redirect

class NewRestaurantView(CreateView):
    template_name = 'new_restaurant.html'
    form_class = RestaurantForm

    def form_invalid(self, form):
        return super().form_invalid(form)