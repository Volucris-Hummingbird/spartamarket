from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        
class ImageuploadForm(forms.ModelForm):
    image = forms.ImageField(label='image')
    


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         exclude = ("article", "user")
