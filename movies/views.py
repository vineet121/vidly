from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    output=', '.join([m.title for m in movies])
    return HttpResponse(output)

# Create your views here.
