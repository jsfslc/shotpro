from django.urls import path
from backoffice import views
from .views import ListPostsView, DetailPostView,  UpdatePostView, DeletePostView

urlpatterns = [
  path('', views.index, name= 'backoffice'),
  path('profile',views.profile, name= 'profile'),
  # path('edit_profile/',UpdateUserView.as_view(), name= 'edit_profile'),
  path('logout',views.logout_view, name='logout'),
  path('posts/',ListPostsView.as_view(), name='posts'),
  path('posts/<int:pk>',DetailPostView.as_view(), name='detail_post'),
  path('posts/create',views.createPost, name='create_post'),
  # path('posts/create',CreatePostView.as_view(), name='create_post'),
  path('posts/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
  path('posts/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]