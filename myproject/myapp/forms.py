from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_time', 'image', 'ingredients']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4}),
        }