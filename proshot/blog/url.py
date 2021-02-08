
from django.urls import path, include
from blog import views

urlpatterns = [
  path('', views.index, name= "index"),
  path('<int:id>/', views.detail_view, name='detail'),
  path('login', views.login_view, name='login'),
  path('testing', views.testing_website, name='testing'),
  path('work-with-us',views.workwithus_view, name="workwithus")
]