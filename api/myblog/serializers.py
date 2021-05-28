from rest_framework import serializers
from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
)

import logging, pytz
from datetime import (
    datetime,
    timezone,
    timedelta
)

from django.utils import timezone as timezone_django
from django.db.models import Q

from .utils import (
    utc_to_jst,
)


logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %'(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')

logger = logging.getLogger(__name__)



class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = mUser
        fields = [
            'username',
            'email',
        ]


class BlogSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Blog
        fields = [
            'title',
            'user',
        ]


class CategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'user',
            'slug',
        ]


class TagSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Tag
        fields = [
            'name',
            'user',
            'slug',
        ]


class PostSerializer(DynamicFieldsModelSerializer):

    content = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'blog',
            'title',
            'content',
            'category',
            'tags',
            'thumbnail',
            'is_public',
        ]

    def get_content(self, obj):
        return obj.convert_markdown_to_html()


class CommentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'name',
            'text',
            'email',
            'post',
            'is_public',
        ]
