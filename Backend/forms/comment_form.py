from django import forms
from Backend.models.comment import Comment

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('content', 'rate')
        labels = {
            'content':'Give feedback',
            'rate':'Give your rate'
        }