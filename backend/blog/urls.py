from django.contrib import admin
from django.urls import path, include
from .views import ArticleList, ArticleDetail, ArticleDetailBySlug

app_name: str = "blog"

urlpatterns: list = [
    path("", ArticleList.as_view(), name='list'),
    path("<int:pk>", ArticleDetail.as_view(), name="detail"),
    path("<slug:slug>", ArticleDetailBySlug.as_view(), name="detail-by-slug"),
]
