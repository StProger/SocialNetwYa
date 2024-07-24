from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index():

    return HttpResponse("Главная страница")


def group_posts(slug: str):

    return HttpResponse(f"Группа: {slug}")
