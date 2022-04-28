from rest_framework import serializers

from blog.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields: list[str] = ["id", "username", "first_name", "last_name"]


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        # fields: tuple[str] = ("title", "slug", "author", "content", "publish_datetime", "status")
        exclude: tuple[str] = ("creation_datetime", "last_update_datetime")
        # fields: str = "__all__"

    def validate_title(self, value):
        filter_list: list[str] = ["javascript", "laravel", "PHP"]
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Don't use bad words! : {}".format(i))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        model = get_user_model()
        fields: str = "__all__"
