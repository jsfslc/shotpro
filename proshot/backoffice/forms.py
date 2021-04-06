from django import forms
from django.forms import inlineformset_factory
from blog.models import Post, PostPicture
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','content',)

    widget = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'content': forms.Textarea(attrs={'class': 'form-control'}),
    }

class PicturesForm(forms.ModelForm):
  class Meta:
    model = PostPicture
    fields = ('image','image_name')

    widget = {
      'pictures': forms.ImageField(label='image')
    }

# PostPicturesFormSet = inlineformset_factory(Post, 
#   PostPicture,
#   fields=('image', 'image_name'),
#   extra=1,
#   max_num=1,
#   widgets={
#     'image_name':
#     forms.TextInput(attrs={'placeholder': 'Image name'})
#   }
# )


class UserLoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput())
  password = forms.CharField(widget=forms.PasswordInput())


class UserEditForms(forms.ModelForm):
  first_name= forms.CharField(min_length = 4, max_length=50, label = "First Name")
  last_name= forms.CharField(min_length=4, max_length=50, label = "Last name")
  email = forms.EmailField(max_length=200, label = "Email address")

  class Meta:
    model = User
    fields= ('first_name', 'last_name', 'email')

  def clean_email(self):
    email = self.cleaned_data['email']
    current_user =  self.instance.pk

    if User.objects.filter(email=email).exists():
      if current_user != User.objects.get(email=email).id:
        raise forms.ValidationError(
          'Este correo ya está siendo utilizado, porfavor ingresa otro correo'
        )
    return email
  
class PwdChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label = 'Old password',widget=forms.PasswordInput())
  new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput())
  new_password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput())

