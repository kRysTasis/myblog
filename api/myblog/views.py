from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .models import (
    Post
)
from .serializers import (
    PostSerializer
)
from .filters import (
    PostFilter
)

class SearchView(generics.ListAPIView):

    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True
            )
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(
            queryset,
            many=True
        )
        return Response(serializer.data)
