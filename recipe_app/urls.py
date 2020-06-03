from django.urls import path
from recipe_app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('authors/<int:id>/', views.authors, name="authors"),
    path('recipes/<int:id>/', views.recipes, name="recipes"),
    path('addauthor/', views.add_author, name='addauthor'),
    path('addrecipe/', views.add_recipe, name='addrecipe'),
    path('editrecipe/<int:id>/', views.edit_recipe, name='editrecipe'),
    path('favorite/<int:id>/', views.toggle_favorite, name='favorite'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
