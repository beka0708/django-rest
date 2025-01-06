from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CustomUser
from .serializers import UserSerializer


class UserListAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

