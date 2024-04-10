from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="post-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("authors", views.allauthor,name="allauthor"),
    path("authors/<slug:author>", views.author, name="author-page"),  # Add a prefix "authors/"
]
