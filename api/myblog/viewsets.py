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

    pass


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


class CommentViewSet(BaseModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
