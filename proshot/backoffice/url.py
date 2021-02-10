from django.urls import path
from backoffice import views

urlpatterns = [
  path('dashboard', views.index, name= 'backoffice'),
  path('logout',views.logout_view, name='logout')
]