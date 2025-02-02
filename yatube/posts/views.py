from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def group_posts(request, slug):

    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        "text": "Здесь будет информация о группах проекта Yatube",
        "posts": posts,
        "group": group
    }
    return render(request, template, context)


def index(request):

    template = "posts/index.html"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        "text": "Это главная страница проекта Yatube",
        "posts": posts
    }
    return render(request, template, context)