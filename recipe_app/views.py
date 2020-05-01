from django.shortcuts import render
from recipe_app.models import Recipe
from recipe_app.models import Author


# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'main.html', {'data': data})


def recipes(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipes.html', {'recipe': data})


def authors(request, id):
    data_a = Author.objects.get(id=id)
    data_r = Recipe.objects.filter(author_id=id)
    return render(request, 'authors.html', {'author': data_a, "recipes": data_r})
