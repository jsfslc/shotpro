from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import permissions, viewsets, mixins
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, PostPictureSerializer
from .models import Post, PostPicture

#ViewSets define the view behavior.
class PostList(APIView):
  """
  A viewset for viewing and editing user instances.
  """
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'index.html'
  ordering_fields = ['created_on']

  def get(self, request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response({'posts': serializer.data})

class PostDetail(APIView):
  """
  A viewset for viewing and editing user instances.
  """
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'detail.html'

  def get(self, request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response({'serializer': serializer, 'post': post})

  def post(self, request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, data=request.data)
    if not serializer.is_valid():
      return Response({'serializer': serializer, 'post': post})
    serializer.save()
    return redirect('index')

class PostCreate(mixins.CreateModelMixin):
  queryset = Post.objects.all()
  serializer = PostSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

def login_view(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

      
    user = authenticate(request, username = username, password= password)

    if user is not None:
      login(request, user)
      return redirect("backoffice")
        
    else:
      print("user doesnt exist")
      messages.info(request, 'Username or password is incorrect')

  return render(request, "login.html")


  #testing pagina
def testing_website(request):
    return render(request,"trying.html")

  
def workwithus_view(request):
    return render(request,"workwithus.html")
