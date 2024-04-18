from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("posts", views.AllPosts.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail-page"),
    path("authors", views.allauthor,name="allauthor"),
    path("authors/<slug:author>", views.author, name="author-page"),  # Add a prefix "authors/"
]
