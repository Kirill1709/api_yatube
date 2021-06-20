from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework import permissions, viewsets

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        #queryset = Comment.objects.filter(post_id=post_id)
        queryset = get_list_or_404(Comment, post_id=post_id)
        comment_id = self.request.query_params.get('comment_id', None)
        if comment_id is not None:
            queryset = get_list_or_404(Comment, id=comment_id)
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(
            author=self.request.user, post=post)
