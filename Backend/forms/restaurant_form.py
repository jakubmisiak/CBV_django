from django import forms
from Backend.models.restaurant import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta():
        model = Restaurant
        fields = ('name', 'address', 'logo', 'category')
        labels = {
            'logo':'Add restaurant logo',
            'category':'Choose restaurant type'
        }