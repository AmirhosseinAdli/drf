# from django.shortcuts import render
# from rest_framework.request import Request
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from .serilizers import ArticleSerializer, UserSerializer

# Create your views here.
from blog.models import Article


# # class ArticleList(ListAPIView):
# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

# class ArticleDetailBySlugView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = "slug"
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self) -> list:
        if self.action in ['list', 'create']:
            permission_classes: list = [IsStaffOrReadOnly]
        else:
            permission_classes: list = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_view_name(self):
        if self.lookup_field == "slug":
            return ArticleDetailBySlugView


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes: tuple = (IsSuperUserOrStaffReadOnly,)
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes: tuple = (IsSuperUserOrStaffReadOnly,)

class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes: tuple = (IsSuperUserOrStaffReadOnly,)

# class RevokeToken(APIView):
#     permission_classes: tuple = (IsAuthenticated,)
#
#     # def get(self, request):
#     #     return Response({"method": "get"})
#     #
#     # def post(self, request):
#     #     return Response({"method": "post"})
#     #
#     # def put(self, request):
#     #     return Response({"method": "put"})
#
#     def delete(self, request: Request) -> Response:
#         request.auth.delete()
#         # return Response({"msg": "Token revoked!"}, status=201)
#         return Response(status=204)
