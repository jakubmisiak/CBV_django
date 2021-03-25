from django.db import models
from django.contrib.auth.models import User
from Backend.models.restaurant import Restaurant


class Comment(models.Model):
    ONE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    VALUES = [
        (ONE,'1'),
        (TWO,'2'),
        (THREE,'3'),
        (FOUR,'4'),
        (FIVE,'5'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=240)
    rate = models.IntegerField(choices=VALUES,null=True)
