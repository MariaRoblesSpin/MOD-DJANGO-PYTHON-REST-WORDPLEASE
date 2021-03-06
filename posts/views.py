from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post


class LatestPostsView(View):
    # Devolviendo una lista de los 5 post mas recientemente publicados. Difiere para usuarios autenticados y no autenticados
    def get(self, request):
        if self.request.user.is_authenticated:
            post = Post.objects.filter(user_id=request.user.id, fecha_publicacion__lte=datetime.now()).order_by('-modification_date')
        else:
            post = Post.objects.filter(fecha_publicacion__lte=datetime.now()).order_by('-modification_date')

        # Creamos el contexto para pasarle los posts a la plantilla y la pk del usuario. Solo se muestran los 5 primeros

        context = {'posts': post[:5]}

        # Crear respuesta HTML con los post
        html = render(request, 'posts/latest.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)

# Mostrando los detalles de un Post


def post_detail(request, pk, name):
    # Recuperar los detalles del post seleccionado de la BD
    post = get_object_or_404(Post.objects.select_related('user'), pk=pk)

    # Crear un contexto para pasar la información del post a la plantilla
    context = {'post': post, 'pk': pk}

    # Renderizar plantilla
    html = render(request, 'posts/detail.html', context)

    # Devolver respuesta HTTP
    return HttpResponse(html)

# Creando un post y evitando que se pueda usar la URL desde el navegador
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Para incluir el id del autor del post. Este se pone por programa y es el de el usuario autenticado.
            new_post = form.save(commit=False)
            new_post.user_id = request.user.id
            new_post.save()
            messages.success(request, 'Post created sucessfully with ID {0}'.format(new_post.pk))
            form = PostForm()
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/new.html', context)


# Mostrar todos los post, en vez de los 5 más recientes
class PostsListView(ListView):

    template_name = 'posts/list.html'
    # model = Post

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            queryset = Post.objects.filter(fecha_publicacion__lte=datetime.now()).order_by('-modification_date')
        elif self.request.user.is_superuser:
            queryset = Post.objects.all().order_by('-modification_date')
        else:
            queryset = Post.objects.filter(user_id=self.request.user.id).order_by('-modification_date')
        return queryset


# Mostrar los blogs que hay en la plataforma
class BlogsListView(ListView):

    template_name = 'posts/blogs.html'
    model = User

# Mostrar los post publicados de un blog
class UserPostsView(View):

    def get(self, request, name):
        # Recuperar los posts del usuario seleccionado.

        post = Post.objects.filter(user__username=name, fecha_publicacion__lte=datetime.now()).order_by('-modification_date')
        # Creamos el contexto para pasarle los posts a la plantilla

        context = {'posts': post}

        # Crear respuesta HTML con los post
        html = render(request, 'posts/posts_user.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)
