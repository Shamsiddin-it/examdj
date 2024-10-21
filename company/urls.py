from django.urls import path
from .views import *

urlpatterns = [
    path("home/",homePageView, name = "home"),
    path("gen/",gen, name = "gen"),
    path("",homePageView, name="home")
]
