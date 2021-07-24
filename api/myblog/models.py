from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from .db.core.models import (
    TimeStampModel,
)
from .db.utils.functional import (
    _get_latest_post
)
import os, uuid, logging

from mdeditor.fields import MDTextField
# from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import markdown


logger = logging.getLogger(__name__)

CATEGORIES = [
    {
        'name': '未分類',
        'slug': 'other'
    },
    {
        'name': 'プログラミング',
        'slug': 'programming'
    },
    {
        'name': '音楽',
        'slug': 'music'
    }
]

TAGS = [
    {
        'name': 'django',
        'slug': 'django'
    },
    {
        'name': 'python',
        'slug': 'python'
    },
    {
        'name': 'dtm',
        'slug': 'dtm'
    },
    {
        'name': 'docker',
        'slug': 'docker'
    },
    {
        'name': '数学',
        'slug': 'math'
    },
    {
        'name': 'life',
        'slug': 'life'
    },
    {
        'name': 'guitar',
        'slug': 'guitar'
    },
    {
        'name': '作曲',
        'slug': 'compose'
    },
]

def createCategories(user):
    logger.debug('カテゴリを生成します。')
    for category in CATEGORIES:
        logger.debug(category)
        try:
            Category.objects.create(
                name=category['name'],
                user=user,
                slug=category['slug']
            )
        except Exception as e:
            logger.error(e)

def createTag(user):
    logger.debug('タグを生成します。')
    for tag in TAGS:
        try:
            Tag.objects.create(
                name=tag['name'],
                user=user,
                slug=tag['slug']
            )
        except Exception as e:
            logger.error(e)


def get_default_blog_name():
    user = mUser.objects.get(is_superuser=True)
    blog = Blog.objects.get(user=user)
    return blog

def get_default_user():
    user = mUser.objects.get(is_superuser=True)
    return user


def get_default_category_name():
    return Category.objects.get(name='未分類')


class AbstractBaseModel(TimeStampModel):

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Username is required field')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        blog = Blog.objects.create(title='myblog', user=user)
        category = Category.objects.create(name='未分類', user=user, slug='other')
        createCategories(user)
        createTag(user)

        return user

    def create_user(self, username, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(username, email, password, **extra_fields)


class mUser(AbstractBaseUser, PermissionsMixin, TimeStampModel):

    username = models.CharField(_('Username'), max_length=70, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=70, unique=True)

    description = models.TextField(_('Description'))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    is_staff = models.BooleanField(
        _('Staff Status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    is_active = models.BooleanField(
        _('Active Flag'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Blog(AbstractBaseModel):

    title = models.CharField(_('Blog Title'), max_length=100)
    user = models.OneToOneField(mUser, on_delete=models.PROTECT, primary_key=True)
    icon = models.ImageField(_('Icon'), upload_to="upload/", blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):

    name = models.CharField(
        _('Category'),
        max_length=100,
        unique=True
    )
    user = models.ForeignKey(
        mUser,
        on_delete=models.CASCADE,
        default=get_default_user,
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')

    def get_latest_post(self):
        queryset = Post.objects.filter(category=self)
        return _get_latest_post(queryset)


class Tag(models.Model):

    name = models.CharField(
        _('Tag'),
        max_length=100
    )
    user = models.ForeignKey(
        mUser,
        on_delete=models.CASCADE,
        default=get_default_user,
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_latest_post(self):
        queryset = Post.objects.filter(tag=self)
        return _get_latest_post(queryset)


class Post(AbstractBaseModel):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        default=get_default_blog_name,
    )
    title = models.CharField(
        _('Title'),
        max_length=255
    )
    # content = MarkdownxField(
    #     _('Content'),
    #     help_text='markdown'
    # )
    content = MDTextField(
        _('Content'),
        help_text='markdown'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=get_default_category_name
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )
    thumbnail = models.ImageField(
        _('Thumbnail'),
        upload_to='upload/',
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        _('Publish or Not'),
        default=False
    )
    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True
    )
    fixed = models.BooleanField(
        _('Fixed post or Not'),
        default=False,
    )
    pickup = models.BooleanField(
        _('Pickup post or Not'),
        default=False,
    )
    from_other_site = models.CharField(
        _('where from'),
        default='qiita',
        max_length=255,
    )

    def __str__(self):
        return self.title

    # def formatted_markdown(self):
    #     return markdownify(self.content)
    #
    # def convert_markdown_to_html(self):
    #     return mark_safe(markdownify(self.content))


class Comment(AbstractBaseModel):

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    text = models.TextField(
        _('Text')
    )
    email = models.EmailField(
        _('Email'),
        max_length=255,
        blank=True,
        null=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    is_public = models.BooleanField(
        _('Publish or Not'),
        default=False
    )

    def __str__(self):
        return self.name


class Work(AbstractBaseModel):

    title = models.CharField(
        _('title'),
        max_length=255,
    )
    description = models.TextField(
        _('description')
    )
    link = models.URLField(
        _('URL')
    )
    thumbnail = models.ImageField(upload_to="upload/")

    def __str__(self):
        return self.title

class WorkImage(AbstractBaseUser):

    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="upload/")
