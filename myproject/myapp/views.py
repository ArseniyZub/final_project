import re
from django.shortcuts import render, redirect

from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RecipeForm

from .forms import *
from .models import *

menu = [{'title': 'Рецепты', 'url': 'all_recipes'},
        {'title': 'Добавить рецепт', 'url': 'add_recipe'}]


def index(request):
    context = {'menu': menu}

    return render(request, 'myapp/index.html', context)


def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'menu': menu, 'title': 'Рецепты', 'recipes': recipes}

    return render(request, 'myapp/recipe_list.html', context)


def recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = IngredientInRecipe.objects.filter(recipe_id=recipe_id)
    context = {'menu': menu, 'title': recipe.title, 'recipe': recipe, 'ingredients': ingredients}

    return render(request, 'myapp/recipe.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()

            ingredients_text = form.cleaned_data['ingredients']
            ingredients_list = ingredients_text.split('\n')
            for ingredient_str in ingredients_list:
                match = re.match(r'(.+?),\s*(\d+)\s*(.*)', ingredient_str)
                if match:
                    ingredient_name = match.group(1)
                    amount = int(match.group(2))
                    unit = match.group(3)
        
                ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name.strip())
                IngredientInRecipe.objects.create(recipe=recipe, ingredient=ingredient, amount=amount)

            return redirect('index')
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'myapp/addrecipe.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'myapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
