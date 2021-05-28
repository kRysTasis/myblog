from django.urls import path, include
from . import views, viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', viewsets.UserViewSet)
router.register('blog', viewsets.BlogViewSet)
router.register('category', viewsets.CategoryViewSet)
router.register('tag', viewsets.TagViewSet)
router.register('post', viewsets.PostViewSet)
router.register('comment', viewsets.CommentViewSet)

app_name = 'myblog'
urlpatterns = [
    path('', include(router.urls)),
]
