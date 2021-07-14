from rest_framework import (
    generics,
    permissions,
    authentication,
    status,
    viewsets,
    filters
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .serializers import (
    UserSerializer,
    BlogSerializer,
    CategorySerializer,
    TagSerializer,
    PostSerializer,
    CommentSerializer,
)

from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
)

from .filters import (
    PostFilter
)

from django.utils import timezone
from datetime import (
    date,
    datetime,
    timedelta,
)

import logging
import requests


logger = logging.getLogger(__name__)



class BaseModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = mUser.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CategoryViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter

    @action(methods=['get'], detail=False)
    def top(self, request):
        logger.debug("topPosts")
        topPosts = Post.objects.filter(fixed=True).order_by("?")[:2]
        pickupPosts = Post.objects.filter(pickup=True).order_by("?")[:3]
        return Response({
            'topPosts': self.get_serializer(topPosts, many=True).data,
            'pickupPosts': self.get_serializer(pickupPosts, many=True).data,
        })

    def list(self, request):
        queryset = self.filter_queryset(
            self.get_queryset().filter(is_public=True).order_by('-created_at'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
