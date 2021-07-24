from django.urls import path, include
from . import views, viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('blogs', viewsets.BlogViewSet)
router.register('categories', viewsets.CategoryViewSet)
router.register('tags', viewsets.TagViewSet)
router.register('posts', viewsets.PostViewSet)
router.register('comments', viewsets.CommentViewSet)
router.register('works', viewsets.WorkViewSet)

app_name = 'myblog'
urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.SearchView.as_view(), name='search'),
]
