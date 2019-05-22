from rest_framework.serializers import ModelSerializer

from posts.models import Post

# Estableciendo los campos que devuelven los endpoints del API


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'text', 'fecha_publicacion']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'text', 'fecha_publicacion', 'categories', 'user']
        read_only_fields = ['id', 'creation_date', 'modification_date']
