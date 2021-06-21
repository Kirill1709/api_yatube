from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')

    def get_text(self, obj):
        return obj.text[:100]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    text = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)

    def get_text(self, obj):
        return obj.text[:100]
