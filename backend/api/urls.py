from django.contrib import admin
from django.urls import path, include
from .views import ArticleList, ArticleDetail, UserDetail, UserList

app_name: str = "api"

urlpatterns: list = [
    path("", ArticleList.as_view(), name='list'),
    path("<int:pk>", ArticleDetail.as_view(), name='detail'),
    path("users/", UserList.as_view(), name='user-list'),
    path("users/<int:pk>", UserDetail.as_view(), name='user-detail'),
]
