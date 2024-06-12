from django.db import models

from django.contrib.auth.models import *
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import *

class Ingredient(models.Model):
    name = models.CharField(max_length=100,)
    unit = models.CharField(max_length=50, )

    def __str__(self):
        return f'{self.name}, {self.unit}'


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    ingredients = models.TextField()

    def __str__(self):
        return self.title


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1, message='min amount = 1')])

    def __str__(self):
        return (
            f'{self.ingredient.name} - {self.amount} {self.ingredient.unit} '
        )
