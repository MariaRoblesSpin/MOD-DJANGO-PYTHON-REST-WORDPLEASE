
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.permissions import UserPermission
from users.serializers import UserListSerializer, UserSerializer, WriteUserSerializer


class UserAPI(ListCreateAPIView):
    permission_classes = [UserPermission]
    # queryset = User.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        order = self.request.query_params.get('ordering', None)
        if order is not None:
            queryset = queryset.order_by(order)
        return queryset

    def get(self, request):
        # users = User.objects.all()
        serializer = UserListSerializer(UserAPI.get_queryset(self), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WriteUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(self.request.POST.get('password'))
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [UserPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = WriteUserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)