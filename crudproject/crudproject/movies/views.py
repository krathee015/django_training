from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import MovieModel

def home(request):
    return HttpResponse("Welcome to home page of Bollywood Movies")

def moviecreate(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form = MovieForm()
    context = {'form': form}
    return render(request,'movies/moviecreate.html',context)

def movielist(request):
    movie = MovieModel.objects.all()
    context = {'object' : movie}
    return render(request,'movies/movie_list.html',context)

def movie_view(request, pk):
    movie= get_object_or_404(MovieModel, pk=pk)
    context = {'object' : movie}
    return render(request, 'movies/movieview.html', context)

def movie_edit(request, pk):
    movie= get_object_or_404(MovieModel, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/movies/movielist/')
    context = {'form': form}
    return render(request, 'movies/moviecreate.html', context)

def movie_delete(request, pk):
    movie = get_object_or_404(MovieModel, pk=pk)
    if request.method=='POST':
        movie.delete()
        return redirect('/movies/movielist/')
    context = {'object': movie}
    return render(request,'movies/moviedelete.html', context)


