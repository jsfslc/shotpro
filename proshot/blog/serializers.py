from rest_framework import serializers

from .models import Person, Post, PostPicture

class PersonSerializer(serializers.ModelSerializer):
  posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
  class Meta:
    model = Person
    fields = (
      'id',
      'first_name',
      'last_name',
      'email',
      'phone',
      'city',
      'region',
      'instagram',
      'portafolio',
      'rutaImagen',
      'idioma',
      'categoriasEspecialidad',
      'disponibilidad',
      'status'
    )

class PostSerializer(serializers.ModelSerializer):
  author = PersonSerializer(required=False, read_only=True)
  serializers.ImageField(use_url=True, required=False, allow_null=True)
  
  class Meta:
    model = Post
    fields = (
      'id',
      'author',
      'title',
      'profilePicture',
      'content',
      'created_on'
    )

class PostPictureSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source='author.username')

  class Meta:
    model = PostPicture
    fields = (
      'id',
      'post',
      'image'
    )