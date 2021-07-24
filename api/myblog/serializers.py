from rest_framework import serializers
from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
    Work,
    WorkImage
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

import markdown


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
            'description',
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
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    category = CategorySerializer()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'blog',
            'title',
            'content',
            'category',
            'tags',
            'thumbnail',
            'is_public',
            'created_at',
            'updated_at',
            'from_other_site',
        ]

    def get_content(self, obj):
        md = markdown.Markdown(
            extensions=[
                'fenced_code',
                'extra',
                'abbr',
                'attr_list',
                'def_list',
                'footnotes',
                'md_in_html',
                'tables',
                'admonition',
                'codehilite',
                'legacy_attrs',
                'legacy_em',
                'nl2br',
                'sane_lists',
                'wikilinks',
                'toc',
                'meta',
                'smarty',
            ],
            extension_configs={
                'toc': {
                    'title': 'Index'
                },
                'smarty': {
                    'smart_angled_quotes': True,
                }
            }
        )
        return md.convert(obj.content)
        # return obj.convert_markdown_to_html()

    def get_created_at(self, obj):
        d = obj.created_at.astimezone(timezone(timedelta(hours=+9)))
        return d.strftime('%Y.%m.%d')

    def get_updated_at(self, obj):
        d = obj.updated_at.astimezone(timezone(timedelta(hours=+9)))
        return d.strftime('%Y.%m.%d %H:%M:%S')

    def get_tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data


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


class WorkSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Work
        fields = [
            'title',
            'description',
            'link',
            'thumbnail',
        ]
