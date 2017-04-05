from django import forms
from .models import Post, Comment


# creates a model form to save the results of the form to the model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'headline', 'text')


#enables users to add comments
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
