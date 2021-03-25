from django.urls import path
from Backend.views.login_view import LoginView
from Backend.views.home_view import HomeView
from Backend.views.logout_view import user_logout
from Backend.views.restaurant_view import RestaurantView
from Backend.views.new_restaurant_view import NewRestaurantView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/',login_required(HomeView.as_view()), name='home'),
    path('logout/',login_required(user_logout) , name='logout'),
    path('restaurant/<int:id>/',login_required(RestaurantView.as_view()) , name='restaurant'),
    path('create-restaurant/', login_required(NewRestaurantView.as_view()), name = 'create_restaurant')
]
