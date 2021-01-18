from django.contrib import admin

from .models import Post, PostPicture

class PostPictureAdmin(admin.StackedInline):
  model=PostPicture

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  inlines = [PostPictureAdmin]

  class Meta:
    model=Post

@admin.register(PostPicture)
class PostPictureAdmin(admin.ModelAdmin):
  pass

# Register your models here.
