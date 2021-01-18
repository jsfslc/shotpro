from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name= "index"),
  path('', views.blog_view, name='blog'),
  path('<int:id>/', views.detail_view, name='detail'),
]