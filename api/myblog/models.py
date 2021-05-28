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
    _get_latest_post,
)
import os, uuid, logging

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

logger = logging.getLogger(__name__)



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

class Category(AbstractBaseModel):

    name = models.CharField(_('Category'), max_length=100, unique=True)
    user = models.ForeignKey(mUser, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')

    def get_latest_post(self):
        queryset = Post.objects.filter(category=self)
        return _get_latest_post(queryset)


class Tag(AbstractBaseModel):

    name = models.CharField(_('Tag'), max_length=100)
    user = models.ForeignKey(mUser, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        queryset = Post.objects.filter(tag=self)
        return _get_latest_post(queryset)


class Post(AbstractBaseModel):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    content = MarkdownxField(_('Content'), help_text='markdown')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    thumbnail = models.ImageField(_('Thumbnail'), upload_to='upload/', blank=True, null=True)
    is_public = models.BooleanField(_('Publish or Not'), default=False)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.content)

    def convert_markdown_to_html(self):
        return mark_safe(markdownify(self.content))


class Comment(AbstractBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(_('Text'))
    email = models.EmailField(_('Email'), max_length=255, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_public = models.BooleanField(_('Publish or Not'), default=False)

    def __str__(self):
        return self.name
