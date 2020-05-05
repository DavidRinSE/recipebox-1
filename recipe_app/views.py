from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm


# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'main.html', {'data': data})


def recipes(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipes.html', {'recipe': data})


def add_auhor(request):
    pass


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'], author=data['author'], description=data['description'], time_required=data['time_required'], instructions=data['instructions'])
            return HttpResponseRedirect(reverse('home'))

    form = AddRecipeForm()

    return render(request, 'add_recipe_form.html', {'form': form})


def authors(request, id):
    data_a = Author.objects.get(id=id)
    data_r = Recipe.objects.filter(author_id=id)
    return render(request, 'authors.html', {'author': data_a, "recipes": data_r})
