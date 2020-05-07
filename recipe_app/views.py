from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm


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


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm()

    return render(request, 'add_author_form.html', {'form': form})


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


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()

    return render(request, 'login.html', {'form': form})
