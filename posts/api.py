from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from datetime import datetime
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostsQueryAPI(object):
    # Lectura de los posts de un usuario o de un post por clave.
    #   - Si el usuario no está autenticado se leen todos los posts de usuario seleccionado
    #   - Si el usuario está autenticado se leen todos sus posts, publicados o no
    #   - Si el usuario autenticado es administrador se leen todos los posts del usuario
    def get_queryset(self):
        if self.kwargs.get('name') is not None:
            if self.request.user.is_authenticated and self.request.user.username == self.kwargs.get('name'):
                queryset = Post.objects.filter(user_id=self.request.user.id).order_by('-modification_date')
            elif self.request.user.is_superuser:
                queryset = Post.objects.filter(user__username=self.kwargs.get('name')).order_by('-modification_date')
            else:
                queryset = Post.objects.filter(user__username=self.kwargs.get('name'), fecha_publicacion__lte=datetime.now()).order_by('-modification_date')
        else:
            queryset = Post.objects.filter(pk=self.kwargs.get('pk'))
        return queryset


class PostsAPI(PostsQueryAPI, ListCreateAPIView):
    # Devolver una lista de Post o permitir añadir un Post
    permission_classes = [PostPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'fecha_publicacion']

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostDetailAPI(PostsQueryAPI, RetrieveUpdateDestroyAPIView):
    # Devolver los datos de un Post y permitir modificarlo y borrarlo
    permission_classes = [PostPermission]
    serializer_class = PostSerializer

