from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        labels = {'message': '내용'}
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'class': 'form-control',
                'placeholder': '댓글을 입력하세요'
            })
        }

