from django import forms
from django.contrib.auth.models import User
from .models import Recipe

class RecipeForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_time', 'image', 'author']
