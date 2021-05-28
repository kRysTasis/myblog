from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment
)


admin.site.register(mUser)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)
