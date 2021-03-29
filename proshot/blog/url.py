
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import PwdResetForm, PwdResetConfirmForm


app_name = 'blog'

urlpatterns = [
  path('', views.PostList.as_view(), name="index"),
  path('posts/<int:id>/', views.PostDetail.as_view(), name="detail"),
  # #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  #path('login', views.login_view, name='login'),
  path('testing', views.testing_website, name='testing'),
  path('work-with-us',views.accounts_register, name="workwithus"),
  path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name="activate"),
  path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html',
                                                              form_class=PwdResetForm), name='pwdreset'),
  path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
    template_name='registration/password_reset_confirm.html', form_class=PwdResetConfirmForm ), name= "pwdresetconfirm"),
]
urlpatterns = format_suffix_patterns(urlpatterns)