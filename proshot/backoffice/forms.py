from django import forms
from django.forms import inlineformset_factory
from blog.models import Post, PostPicture

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','content',)

    widget = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'content': forms.Textarea(attrs={'class': 'form-control'}),
    }

PostPicturesFormSet = inlineformset_factory(Post, 
  PostPicture,
  fields=('image', 'image_name'),
  extra=1,
  max_num=1,
  widgets={
    'image_name':
    forms.TextInput(attrs={'placeholder': 'Image name'})
  }
)
