from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Author,Blog,Tags
all_post=Blog.objects.all()
all_author=Author.objects.all()

def starting_page(request):
    # Sort blog posts by date
    sorted_posts = sorted(all_post, key=lambda post: post.date, reverse=True)
    
    # Get the latest three posts
    latest_posts = sorted_posts[:3]
    
    return render(request, "blog/index.html", {
        "posts": latest_posts  # Pass latest_posts instead of all_post
    })
    
def posts(request):    
    return render(request,"blog/all-posts.html",{
        "all_post":all_post
    })
def post_detail(request, slug):
    identified_post=next(post for post in all_post if post.slug==slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post,
        "post_tags":identified_post.tags.all()
    })
# def author(request, author):
#     identified_author = get_object_or_404(Author, firstname=author)
#     return render(request, "blog/author.html", {"author": identified_author})
def author(request, author):
    identified_author = next(auth for auth in all_author if auth.firstname == author)
    return render(request, "blog/author.html", {"author": identified_author})

def allauthor(request):
    return render(request,"blog/all-authors.html",{
        "all_author":all_author
    })