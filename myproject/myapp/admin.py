from django.contrib import admin

from django.contrib import admin

from .models import *


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'cooking_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')
    list_display_links = ('name',)
    search_fields = ('name',)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    list_display_links = ('id', 'recipe')
    search_fields = ('recipe', 'ingredient')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
