from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'), 
    path('recipes/', all_recipes, name='all_recipes'), 
    path('recipes/<int:recipe_id>/', recipe_by_id, name='recipe_by_id'), 
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('addrecipe', add_recipe, name='add_recipe')
]