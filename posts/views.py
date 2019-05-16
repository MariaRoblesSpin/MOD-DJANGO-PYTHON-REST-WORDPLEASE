
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post


class LatestPostsView(LoginRequiredMixin, View):

    def get(self, request):
        # Recuperar los últimas post de la base de datos del usuario autenticado
        if self.request.user.is_superuser:
            post = Post.objects.all().order_by('-modification_date')
        else:
            post = Post.objects.filter(user_id=request.user.id).order_by('-modification_date')

        # Creamos el contexto para pasarle los posts a la plantilla y la pk del usuario
        # para que solo se muestren los post del usuario autenticado

        context = {'blogs': post[:5]}

        # Crear respuesta HTML con los post
        html = render(request, 'posts/latest.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)

@login_required
def post_detail(request, pk):
    # Recuperar los detalles del post seleccionadd de la BD
    post = get_object_or_404(Post.objects.select_related('user'), pk=pk)

    # Crear un contexto para pasar la información del post a la plantilla
    context = {'post': post, 'pk': pk}

    # Renderizar plantilla
    html = render(request, 'posts/detail.html', context)

    # Devolver respuesta HTTP
    return HttpResponse(html)


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user.id
            new_post.save()
            messages.success(request, 'Post created sucessfully with ID {0}'.format(new_post.pk))
            form = PostForm()
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/new.html', context)


class PostsListView(ListView):

    template_name = 'posts/list.html'
    # model = Post

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Post.objects.all().order_by('-modification_date')
        else:
            queryset = Post.objects.filter(user_id=self.request.user.id).order_by('-modification_date')
        return queryset


