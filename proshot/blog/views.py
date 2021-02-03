from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Post, PostPicture

def detail_view(request, id):
  post = get_object_or_404(Post, id=id)
  photos = PostPicture.objects.filter(post=post)
  return render(request, 'detail.html', {
    'post':post,
    'photos':photos
  })

# Create your views here.
def index(request):
    
    posts = Post.objects.all()
    return render(request, "index.html", {'posts':posts}) 


def login_view(request):
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      print(username)
      print(password)     
      user = authenticate(request, username = username, password= password)

      if user is not None:
        login(request, user)
        return redirect("backoffice")
        
      else:
        print("user doesnt exist")
        messages.info(request, 'Username or password is incorrect')

    return render(request, "login.html")

    

