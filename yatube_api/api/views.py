from api.permissions import IsOwnerOrReadOnlyPermission
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import permissions, viewsets


class PostViewSet(viewsets.ModelViewSet):
    """
    Поддерживает CRUD операции:
    GET, POST, PATCH, DELETE, UPDATE
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnlyPermission
    ]

    def perform_create(self, serializer):
        """При создании поста, автоматически присваиваем автора."""
        serializer.save(
            author=self.request.user,
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Только для чтения."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnlyPermission
    ]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        post = self.get_post()
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(
            author=self.request.user,
            post=post,
        )
