from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet,CharacterViewSet,AuthorViewSet

router = routers.DefaultRouter()
router.register("books",BookViewSet)
router.register("characters",CharacterViewSet)
router.register("authors",AuthorViewSet)
urlpatterns = [
    path("",include(router.urls))

]