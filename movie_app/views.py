from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Avg, Max, Min, Count, Value
from django.views.generic import ListView,DetailView


# Create your views here.
def show_movies(request):
    # movies = Movie.objects.order_by('-rating')

    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        new_salary=F('salary') + 200,
        new_rating=F('rating') + 10).annotate(new_year=F('rating') + F('year'))


    filtred_movie = Movie.objects.exclude(year__isnull=True).filter(salary__lt=5000000)
    agg = Movie.objects.aggregate(Count('name'), Sum('salary'), Avg('salary'), Min('rating'), Max('rating'))
    return render(request, 'movie_app/all_movie.html', {'movies': movies,
                                                        'agg': agg, 'total': movies.count(),
                                                        'filtred_movie': filtred_movie})


def show_one_movie(request, slug_id: str):
    movie = get_object_or_404(Movie, slug=slug_id)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


# def show_all_directors(request):
#     directors = Director.objects.all()
#     return render(request, 'movie_app/all_directors.html', {'directors': directors,
#                                                             })
class Alldirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


# def one_director(request, id_dir: int):
#     dir = get_object_or_404(Director, id=id_dir)
#     return render(request, 'movie_app/one_director.html', {'dir': dir})

class OneDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'dir'


# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', context={
#         'actors': actors
#     })

class Allactors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


# def one_actor(request, id_act: int):
#     act = get_object_or_404(Actor, id=id_act)
#     return render(request, 'movie_app/one_actor.html', {'act': act})

class OneActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'act'
