from django.urls import path
from recipe_app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipes"),
    path('authors/<int:id>/', views.authors, name="authors"),
]
