from django import forms
from .models import Post, Comment

class SearchForm(forms.ModelForm):

    class Meta:
	    model = Post
	    fields = ('post',)


class PostForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter the Type of Post'
	}
	))
	post = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter your Blog post'
	}
	))

	class Meta:
		model = Post
		fields = ('post','title')

class CommentForm(forms.ModelForm):
	text = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter your Comment'
	}
	))

	class Meta:
		model = Comment
		fields = ('text',)
