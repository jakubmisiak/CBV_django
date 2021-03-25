from django.db import models


class Restaurant(models.Model):
    KEBAB = 'Kebab'
    ITALIAN = 'Italian'
    ASIAN = 'Asian'
    SUSHI = 'Sushi'
    POLISH = 'Polish'
    BURGER = 'Burger'
    VEGAN = 'VEGAN'
    VALUES =[
        (KEBAB,'Kebab'),
        (ITALIAN, 'Italian'),
        (ASIAN, 'Asian'),
        (SUSHI, 'Sushi'),
        (POLISH, 'Polish'),
        (BURGER, 'Burger'),
        (VEGAN, 'VEGAN')
    ]
    
    
    name = models.CharField(max_length=50)
    address =  models.CharField(max_length=50)
    logo =  models.ImageField(upload_to='logos', blank=True, null=True)
    category = models.CharField(choices=VALUES, max_length=15, null=True)

    def get_absolute_url(self):
        return f"/restaurant/{self.id}"