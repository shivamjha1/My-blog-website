from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect 
from datetime import date
from django.views.generic import ListView,DetailView,View
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



class PostDetail(View):
    
    def get(self,request,slug):
        blog=Blog.objects.get(slug=slug)
        context={
            "post":blog,
            "post_tags":blog.tags.all(),
            "comment_form":CommentForm(),
            "comments":blog.comments.all().order_by("-id") 
        }
        return render(request,"blog/post-detail.html",context)
    
    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.blog=Blog.objects.get(slug=slug)
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        blog=Blog.objects.get(slug=slug)
        context={
            "post":blog,
            "post_tags":blog.tags.all(),
            "comment_form":CommentForm(),
            "comments":blog.comments.all().order_by("-id")    
        }
        return render(request,"blog/post-detail.html",context)
      
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