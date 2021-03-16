from django.urls import path
from backoffice import views

urlpatterns = [
  path('', views.index, name= 'backoffice'),
  path('profile',views.profile, name= 'profile'),
  path('logout',views.logout_view, name='logout')
]