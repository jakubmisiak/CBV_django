from django.views.generic import View
from Backend.models.restaurant import Restaurant
from Backend.models.comment import Comment
from Backend.forms.comment_form import CommentForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


class RestaurantView(View):
    def get(self, request, id):
        form = CommentForm()
        resteurant = Restaurant.objects.get(id=id)
        comments = Comment.objects.all().filter(restaurant=resteurant).order_by('-id')
        print(resteurant.id)
        context = {
            'restaurant':resteurant,
            'form':form,
            'comments':comments,
        }
        return render(request, 'restaurant.html', context) 
    
    def post(self, request, id):
        form = CommentForm(request.POST, request.FILES)
        current_user = request.user
        current_resteurant = Restaurant.objects.get(id=id)
        print(current_resteurant.name)
        print(current_resteurant.id)
        if form.is_valid():
            comment = form.save()
            comment.restaurant = current_resteurant
            comment.user = current_user
            comment.save()
        return redirect('restaurant', id=current_resteurant.id)

