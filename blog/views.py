from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView

from .models import Author,Blog,Tags,Comments
from .forms import CommentForm
all_post=Blog.objects.all()
all_author=Author.objects.all()


#view classes
class StartingPage(ListView):
    template_name="blog/index.html"
    model=Blog
    ordering=["-date"]
    context_object_name="posts"
    
    def get_queryset(self) -> QuerySet[Any]:
        querySet= super().get_queryset()
        data=querySet[:3]
        return data    

# def starting_page(request):
#     sorted_posts = Blog.objects.all().order_by("-date")[:3]
#     latest_posts = sorted_posts[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts  # Pass latest_posts instead of all_post
#     })
    
    
class AllPosts(ListView):
    template_name="blog/all-posts.html"
    model=Blog
    ordering=["-date"]
    context_object_name="all_post"
# def posts(request):    
#     return render(request,"blog/all-posts.html",{
#         "all_post":all_post
#     })



class PostDetail(DetailView):
    template_name="blog/post-detail.html"
    model=Blog
    context_object_name="post"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context["post_tags"]=self.object.tags.all()
        context["comment_form"]=CommentForm()
        return context
      
# def post_detail(request, slug):
#     identified_post=next(post for post in all_post if post.slug==slug)
#     return render(request, "blog/post-detail.html",{
#         "post": identified_post,
#         "post_tags":identified_post.tags.all()
#     })




def author(request, author):
    identified_author = next(auth for auth in all_author if auth.firstname == author)
    return render(request, "blog/author.html", {"author": identified_author})

def allauthor(request):
    return render(request,"blog/all-authors.html",{
        "all_author":all_author
    })