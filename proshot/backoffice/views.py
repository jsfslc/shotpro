from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from .forms import PostForm, PostPicturesFormSet


# Create your views here.

def index(request):
    print("back office")
    return render(request, "dashboard.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def profile(request):
    print("profile")
    return render(request, "profile.html")

class ListPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    ordering = ['-created_on']

class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail-post.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # postpictures_form = PostPicturesFormSet(self.request.POST)
        if (form.is_valid() ):
          return self.form_valid(form, )
        else:
          return self.form_invalid(form, )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.person
        # postpictures_form.instance = obj
        # postpictures_form.save()
        obj.save()
        return reverse('posts')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update-post.html'

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('posts')