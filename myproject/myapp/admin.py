from django.contrib import admin
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'cooking_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')

admin.site.register(Recipe, RecipeAdmin)

