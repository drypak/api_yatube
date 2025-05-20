from rest_framework import viewsets
from rest_framework import permissions
from posts.models import Comment, Post, Group
from django.shortcuts import get_object_or_404
from api.serializers import CommentSerializer, PostSerializer, GroupSerializer
from api.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    """
    Поддерживает CRUD операции:
    GET, POST, PATCH, DELETE
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """при создании поста, автоматически присваиваем автора."""
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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):

        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
