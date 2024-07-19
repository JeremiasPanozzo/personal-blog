from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.

#Obtiene todas las publicaciones de la base de datos
def blog_index(request):
    #order_by() ordena por created_on, el - significa de mayor a menor
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

#Obtiene todos los posts de una determinada categoria
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blogcategory.html", context)

#Solicita un post determinado mediante du primary key
def blog_detail(request, pk):

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/detail.html", context)