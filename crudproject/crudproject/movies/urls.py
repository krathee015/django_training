from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

path('home/',views.home,name ='home'),
path('moviecreate/',views.moviecreate, name ="MC"),
path('movielist/',views.movielist, name ="ML"),
path('movieview/<int:pk>',views.movie_view, name ="MV"),
path('movieedit/<int:pk>',views.movie_edit, name ="ME"),
path('moviedel/<int:pk>',views.movie_delete, name ="MD"),
]