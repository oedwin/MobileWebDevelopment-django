from django import forms
from .models import Post


# creates a model form to save the results of the form to the model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'headline', 'text')
