from django.urls import path
from backoffice import views
from .views import ListPostsView, DetailPostView, CreatePostView, UpdatePostView, DeletePostView
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdChangeForm


app_name = 'backoffice'

urlpatterns = [
  path('', views.index, name= 'backoffice'),
  path('profile',views.profile, name= 'profile'),
  path('logout',views.logout_view, name='logout'),
  path('posts/',ListPostsView.as_view(), name='posts'),
  path('posts/<int:pk>',DetailPostView.as_view(), name='detail_post'),
  path('posts/create',CreatePostView.as_view(), name='create_post'),
  path('posts/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
  path('posts/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),

  path('login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                              authentication_form =UserLoginForm), name='login'),
  
                
                            
]