from . import views
from django.urls import path

urlpatterns = [

    path('', views.show_movies),
    path('movie/<slug:slug_id>', views.show_one_movie, name='movie-id'),
    path('directors/', views.Alldirectors.as_view(),name='directors-all'),
    path('directors/<int:pk>', views.OneDirector.as_view(), name='one-dir'),
    path('actors/', views.Allactors.as_view(),name='actors-all'),
    path('actors/<int:pk>', views.OneActor.as_view(), name='one-actor'),
]
