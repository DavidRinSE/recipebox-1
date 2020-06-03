from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm


# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'main.html', {'data': data})


def recipes(request, id):
    data = Recipe.objects.get(id=id)
    loggedin = False
    if request.user:
        loggedin = True
    edit = False
    if request.user and (request.user.is_staff or request.user.author == data.author):
        edit = True
    return render(request, 'recipes.html', {'recipe': data, 'edit': edit, 'loggedin': loggedin})


def authors(request, id):
    data_a = Author.objects.get(id=id)
    data_f = data_a.favorites.all()
    data_r = Recipe.objects.filter(author_id=id)
    return render(request, 'authors.html', {'author': data_a, "recipes": data_r, "favorites":data_f})


@login_required
def add_author(request):
    if not request.user.is_staff:
        return render(request, 'error.html', {'usr_auth': False})
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password'])
            Author.objects.create(
                name=data['name'], username=data['username'], user=user, bio=data['bio'])
        return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm()

    return render(request, 'add_author_form.html', {'form': form})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'], author=data['author'], description=data['description'], time_required=data['time_required'], instructions=data['instructions'])
            return HttpResponseRedirect(reverse('home'))

    form = AddRecipeForm(user=request.user)

    return render(request, 'add_recipe_form.html', {'form': form})


@login_required
def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":
        form = AddRecipeForm(request.POST, user=request.user)
        if form.is_valid():
            data = form.cleaned_data

            recipe.title = data["title"]
            recipe.author = data["author"]
            recipe.description = data["description"]
            recipe.time_required = data["time_required"]
            recipe.instructions = data["instructions"]

            recipe.save()
            return HttpResponseRedirect(reverse("recipes", kwargs={"id": id}))

    if request.user.is_superuser or request.user.author == recipe.author:
        form = AddRecipeForm(initial={
            "title": recipe.title,
            "author": recipe.author.id,
            "description": recipe.description,
            "time_required": recipe.time_required,
            "instructions": recipe.instructions
        }, user=request.user)
        return render(request, 'edit_recipe_form.html', {"form": form})
    else:
        return HttpResponseRedirect(reverse("recipes", kwargs={"id": id}))


@login_required
def toggle_favorite(request, id):
    author = request.user.author

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        HttpResponseRedirect("/")

    if recipe in author.favorites.all():
        author.favorites.remove(recipe)
    else:
        author.favorites.add(recipe)
    author.save()
    return HttpResponseRedirect(reverse("recipes", kwargs={"id": id}))


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))

    form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
