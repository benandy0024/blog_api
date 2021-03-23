from django.shortcuts import render
from rest_framework import generics
from .models import Post
from.serializers import PostSerializer
# Create your views here.
class PostViewCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostViewDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer