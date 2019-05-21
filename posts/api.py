from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostsList


class PostsAPI(PostsList, ListCreateAPIView):

    permission_classes = [PostPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'fecha_publicacion']

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostDetailAPI(PostsList, RetrieveUpdateDestroyAPIView):

    permission_classes = [PostPermission]
    serializer_class = PostSerializer

