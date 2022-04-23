from django.contrib import admin
from django.urls import path, include
# from .views import ArticleList, ArticleDetail, UserDetail, UserList, ArticleDetailBySlugView
from rest_framework import routers

from .views import ArticleViewSet, UserViewSet

app_name: str = "api"

# urlpatterns: list = [
#     path("", ArticleList.as_view(), name='list'),
#     path("<int:pk>", ArticleDetail.as_view(), name='detail'),
#     path("<slug:slug>", ArticleDetailBySlugView.as_view(), name='detail-by-slug'),
#     path("users/", UserList.as_view(), name='user-list'),
#     path("users/<int:pk>", UserDetail.as_view(), name='user-detail'),
# ]

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename="articles")
router.register('users', UserViewSet, basename="users")

# urlpatterns = router.urls

urlpatterns: list = [
    path("", include(router.urls)),
]
