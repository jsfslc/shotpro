
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include

urlpatterns = [
  path('', views.PostList.as_view()),
  path('posts/<int:pk>/', views.PostDetail.as_view()),
  #path('', views.index, name= "index"),
  #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  #path('<int:id>/', views.detail_view, name='detail'),
  path('login', views.login_view, name='login'),
  path('testing', views.testing_website, name='testing'),
  path('work-with-us',views.workwithus_view, name="workwithus")
]

urlpatterns = format_suffix_patterns(urlpatterns)