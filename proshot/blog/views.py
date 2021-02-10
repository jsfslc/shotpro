from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from .serializers import PostSerializer, PostPictureSerializer
from .models import Post, PostPicture

# ViewSets define the view behavior.
class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all().order_by('-created_on')
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
  #return render(request, "index.html", {'posts':posts}) 

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer