from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('v1/', include(router.urls)),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comments-list'
    ),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comments-list'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve', 
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'destroy',
        }),
        name='comments-detail'
    ),
]
