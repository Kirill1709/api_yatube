from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, UserViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
