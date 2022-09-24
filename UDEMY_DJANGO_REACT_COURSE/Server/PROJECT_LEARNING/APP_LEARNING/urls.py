from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views
from .views import Another,BookViewSet


router = routers.DefaultRouter()
router.register('books',BookViewSet)

urlpatterns = [
    #path("",views.first),
    path("getallbooks",Another.as_view()),
    path("getpublishedbooks",views.only_published_book),
    path("getsinglebook",views.get_only_books),
    path("rendermyhtml",views.rendermyhtml),
    path("renderdynamic",views.renderdynamictemplate),
    path("",include(router.urls))
]
