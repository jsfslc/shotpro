from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

# Create your views here.
def index(request):
    
    posts = Post.objects.all()
    return render(request, "index.html", {'posts':posts}) 


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
