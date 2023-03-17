from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movies

# data = {
#     'movies': [
#     {
#         'id': 5,
#         'title': 'Jaw',
#         'year': 1669
#     },
#     {
#        'id': 6,
#         'title': 'Sharknado',
#         'year': 1660 
#     },
#     {
#         'id': 7,
#         'title': 'The Mag',
#         'year': 2000
#     }

#     ]
# }


def movies(request):
    data = Movies.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home Page")

def detail(request, id):
    data = Movies.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request): 
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movies(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movies.objects.get(pk=id) 
    except:
        raise Http404('movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')
    
 