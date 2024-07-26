from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):

    template = "posts/index.html"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        "text": "Это главная страница проекта Yatube",
        "posts": posts
    }
    return render(request, template, context)


def group_posts(request):

    template = "posts/group_list.html"
    context = {
        "text": "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)