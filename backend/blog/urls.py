from django.contrib import admin
from django.urls import path, include
from .views import ArticleList

app_name: str = "blog"

urlpatterns: list = [
    path("", ArticleList.as_view(), name='list')
]
