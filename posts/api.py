from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostsList


class PostsAPI(PostsList, ListCreateAPIView):

    queryset = Post.objects.all().order_by('-modification_date')
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [PostPermission]

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostDetailAPI(PostsList, RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all().order_by('-modification_date')
    permission_classes = [PostPermission]
    serializer_class = PostSerializer

