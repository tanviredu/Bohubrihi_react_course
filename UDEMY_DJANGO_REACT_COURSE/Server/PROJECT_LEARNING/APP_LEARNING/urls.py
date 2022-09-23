from django.contrib import admin
from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path("",views.first),
    path("getallbooks",Another.as_view()),
    path("getpublishedbooks",views.only_published_book),
    path("getsinglebook",views.get_only_books)
]
