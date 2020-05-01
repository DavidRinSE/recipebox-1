from django.shortcuts import render
from recipe_app.models import Recipe


# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'main.html', {'data': data})


def recipes(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipes.html', {'data': data})
