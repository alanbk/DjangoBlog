import django_filters
from django.db import models
from .models import Post

class PostFilter(django_filters.FilterSet):
	class Meta:
		model = Post
		fields = ['title',]