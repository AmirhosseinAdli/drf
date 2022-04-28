from rest_framework import serializers

from blog.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields: list[str] = ["id", "username", "first_name", "last_name"]


# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         # return value.first_name + ' ' + value.last_name
#         return value.username


class ArticleSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.username", read_only=True)
    def get_author(self, obj):
        # return str(obj.author.id) + " " + obj.author.username
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    author = serializers.SerializerMethodField("get_author")

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
