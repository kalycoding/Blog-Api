from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions
#from .permissions import IsAuthorOrReadOnly
# Create your views here.


class PostListCreateAPI(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

   

class PostRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
