from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.utils.encoding import *
from django.utils.http import * 
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login

from .serializers import PostSerializer, PostPictureSerializer
from .models import Post, PostPicture
from .forms import RegistrationForm

from .token import account_activation_token



#ViewSets define the view behavior.
class PostList(APIView):
  """
  A viewset for viewing and editing user instances.
  """
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'blog/index.html'
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
  template_name = 'blog/detail.html'

  def get(self, request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response({'serializer': serializer, 'post': post})


"""
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

"""
  #testing pagina
def testing_website(request):
    return render(request,"trying.html")

  
def accounts_register(request):
  if request.method =="POST":
      registerForm = RegistrationForm(request.POST) 
      if registerForm.is_valid():
        user = registerForm.save(commit=False)
        user.email = registerForm.cleaned_data['email']
        user.set_password(registerForm.cleaned_data['password'])
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Activa tu cuenta'
        message = render_to_string('registration/account_activation_email.html',{
          'user':user,
          'domain': current_site.domain,
          'uid':urlsafe_base64_encode(force_bytes(user.pk)),
          'token': account_activation_token.make_token(user),
        })
        user.email_user(subject=subject,message=message)
        return HttpResponse('Registered succesfully and activation sent')
  else:
    registerForm = RegistrationForm()
    
  return render(request,'registration/register.html',{'form' : registerForm})


def activate(request,uidb64,token):
    try:
      uid = force_text(urlsafe_base64_decode(uidb64))
      user = User.objects.get(pk=uid)
    except(TypeError, ValueError,OverflowError, User.DoesNotExist):
      user= None
    if user is not None and account_activation_token.check_token(user, token):
      user.is_active = True
      user.save()
      login(request, user)
      return(redirect('backoffice:login'))
    else:
      return render(request,'registration/activation_invalid.html')
