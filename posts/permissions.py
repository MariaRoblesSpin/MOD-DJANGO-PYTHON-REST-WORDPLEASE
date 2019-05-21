from datetime import datetime

from rest_framework.permissions import BasePermission

from django.utils import timezone
now = timezone.now()


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.method == 'GET' or request.user.is_authenticated
        if request.method == 'POST':
            return request.POST.get('user') == str(request.user.id)
        if request.method == 'PUT' or request.method == 'DELETE':
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            if obj.user == request.user or request.user.is_superuser:
                return True
            else:
                return obj.fecha_publicacion <= now
        if request.method == 'PUT' or request.method == 'DELETE':
            return obj.user == request.user or request.user.is_superuser
