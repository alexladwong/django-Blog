from . import views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # path("", views.home, name="myblogApp-home"),
    path("about/", views.about, name="myblogApp-about"),
    path("", PostListView.as_view(), name="myblogApp-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
    path("post/new", PostCreateView.as_view(), name="myblogApp-new"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="myblogApp-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="blog-delete"),
]
