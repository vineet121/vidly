from typing import NamedTuple
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<movie_id>', views.detail, name ='movies_detail')
]