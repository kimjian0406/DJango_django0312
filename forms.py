from django import forms
from .models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'is_private'] 
from django import forms
from django.forms import modelformset_factory
from .models import Comment


CommentFormSet = modelformset_factory(Comment, fields=('content', 'post'), extra=1)
