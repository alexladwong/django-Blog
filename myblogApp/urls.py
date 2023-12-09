from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="myblogApp-home"),
    path("about/", views.about, name="myblogApp-about"),
]
