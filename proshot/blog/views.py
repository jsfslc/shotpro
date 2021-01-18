from django.shortcuts import render, get_object_or_404

from .models import Post, PostPicture

def blog_view(request):
  posts = Post.objects.all()
  return render(request, 'blog.html', {'posts':posts})

def detail_view(request, id):
  post = get_object_or_404(Post, id=id)
  photos = PostPicture.objects.filter(post=post)
  return render(request, 'detail.html', {
    'posts':post,
    'photos':photos
  })

# Create your views here.
def index(request):
    
    

    return render(request, "index.html") 