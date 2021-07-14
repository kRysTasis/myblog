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

    category = django_filter.CharFilter(
        field_name='category',
        method='category_filter',
    )

    def category_filter(self, queryset, name, value):
        try:
            category = Category.objects.get(slug=value)
        except:
            return queryset

        return queryset.filter(category=category)

    class Meta:
        model = Post
        fields = ['category']
