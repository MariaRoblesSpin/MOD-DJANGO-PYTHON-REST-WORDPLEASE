from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return True
        if request.method == 'PUT' or request.method == 'DELETE':
            return True


    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            if obj.id == request.user.id or request.user.is_superuser:
               return True
        if request.method == 'PUT' or request.method == 'DELETE':
            return obj.id == request.user.id or request.user.is_superuser
