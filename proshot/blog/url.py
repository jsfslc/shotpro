
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.PostList.as_view(), name="index"),
  path('posts/<int:id>/', views.PostDetail.as_view(), name="detail"),
  path('posts/create', views.CreatePost.as_view(), name="create"),
  # #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  path('login', views.login_view, name='login'),
  path('testing', views.testing_website, name='testing'),
  path('work-with-us',views.workwithus_view, name="workwithus")
]
urlpatterns = format_suffix_patterns(urlpatterns)