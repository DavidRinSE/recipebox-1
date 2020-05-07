from django.urls import path
from recipe_app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('authors/<int:id>/', views.authors, name="authors"),
    path('recipes/<int:id>/', views.recipes, name="recipes"),
    path('addauthor/', views.add_author, name='addauthor'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
    path('login/', views.loginview),
]
