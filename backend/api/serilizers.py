from rest_framework import serializers

from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields: tuple[str] = ("title", "slug", "author", "content", "publish_datetime", "status")
        exclude: tuple[str] = ("creation_datetime", "last_update_datetime")
        # fields: str = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: str = "__all__"
