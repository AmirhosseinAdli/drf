# from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serilizers import ArticleSerializer

# Create your views here.
from blog.models import Article


# class ArticleList(ListAPIView):
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
