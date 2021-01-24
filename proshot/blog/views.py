from django.shortcuts import render, get_object_or_404

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