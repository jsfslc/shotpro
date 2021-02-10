from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
  path('', views.PostList.as_view()),
  path('posts/<int:pk>/', views.PostDetail.as_view()),
  #path('', views.index, name= "index"),
  #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  #path('<int:id>/', views.detail_view, name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)