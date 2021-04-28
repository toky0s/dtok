from django.forms import widgets
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.article = kwargs.pop('article', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.article = self.article
        comment.save()
        
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': widgets.TextInput(attrs={
                'placeholder':'Nhập một bình luận...',
                'class':'comment_text'
                })
        }