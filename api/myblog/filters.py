from django.db.models import Q
from django_filters import rest_framework as django_filter
from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
    Work,
    WorkImage,
)

import logging


logger = logging.getLogger(__name__)


class PostFilter(django_filter.FilterSet):

    category = django_filter.CharFilter(
        field_name='category',
        method='category_filter',
    )

    tags = django_filter.CharFilter(
        field_name='tags',
        method='tags_filter',
    )

    text = django_filter.CharFilter(
        method='post_filter'
    )

    class Meta:
        model = Post
        fields = ['category', 'tags']

    def category_filter(self, queryset, name, value):
        try:
            category = Category.objects.get(slug=value)
        except:
            return queryset.none()

        return queryset.filter(category=category)

    def tags_filter(self, queryset, name, value):
        logger.debug('タグのフィルター')
        try:
            logger.debug('tag')
            tag = Tag.objects.get(slug=value).id
            logger.debug(tag)
        except:
            return queryset.none()

        return queryset.filter(tags__in=[tag])

    def post_filter(self, queryset, name, value):
        """
        記事のタイトル、記事の内容、付いてるカテゴリ、付いてるタグに部分一致するものを検索する。
        とりあえず来る文字列はカンマ・スペース区切りは許可しないで1つとみなす。
        """
        queries = [
            Q(title__contains=value),
            # Q(content__contains=value),
            Q(category__name__contains=value),
            Q(tags__name__contains=value),
        ]
        query = queries.pop()
        for q in queries:
            query |= q
        res = Post.objects.filter(query).distinct().order_by('-created_at')

        # title = 'title__contains'
        # content = 'content__contains'
        # res = queryset.filter(Q(**{title:value, content:value}))
        return res
