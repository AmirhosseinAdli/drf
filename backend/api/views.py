# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .serilizers import ArticleSerializer, UserSerializer

# Create your views here.
from blog.models import Article


# class ArticleList(ListAPIView):
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailBySlugView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes: tuple = (IsAdminUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes: tuple = (IsAdminUser,)
