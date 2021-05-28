from django.db.models import Q
from django_filters import rest_framework as django_filter
from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
)

import logging


logger = logging.getLogger(__name__)


class PostFilter(django_filter.FilterSet):

    class Meta:
        model = Post
        fields = []

    pass
