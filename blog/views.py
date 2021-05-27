from django.shortcuts import render, redirect
from .models import Post
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

post_per_page = 3


# Create your views here.
def viewPost(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except:
        return redirect('blog')
    three_lasts = Post.objects.all().order_by('-id')[:3][::-1]
    return render(request, 'pages/post.html', {'post': post, 'newest': three_lasts, 'nav': 'post'})


def sortByAuthor(request, post_author):
    posts_list = Post.objects.filter(author=post_author)
    paginator = Paginator(posts_list, post_per_page)
    pageNumber = request.GET.get('page')
    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/blog.html', {'posts_list': posts, 'nav': 'post'})


def viewAllPost(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, post_per_page)
    pageNumber = request.GET.get('page')
    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/blog.html', {'posts_list': posts, 'nav': 'post'})


def sortByDate(request, date):
    date = date.split('-')
    print(date)
    posts_list = Post.objects.filter(post_date__date=datetime.date(int(date[0]), int(date[1]), int(date[2])))
    return render(request, 'pages/blog.html', {'posts_list': posts_list, 'date': date})


def sortByCategory(request, category):
    posts_list = Post.objects.filter(category=category)
    paginator = Paginator(posts_list, post_per_page)
    pageNumber = request.GET.get('page')
    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'pages/blog.html', {'posts_list': posts})
