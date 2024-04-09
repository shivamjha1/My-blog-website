from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Author,Blog,Tags
all_post=Blog.objects.all()

def starting_page(request):
    # sorted_posts=sorted(all_post)
    # latest_posts=sorted_posts[-3:]
    
    return render(request, "blog/index.html",{
        "posts":all_post
    })

def posts(request):    
    return render(request,"blog/all-posts.html",{
        "all_post":all_post
    })
def post_detail(request, slug):
    identified_post=next(post for post in all_post if post.slug==slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })