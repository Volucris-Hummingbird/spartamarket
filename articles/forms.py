from django import forms
from .models import Article
# from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')
        # 유효성 검사의 항목을 넣어주는 영역이기 때문에 author_id를 건너뛰어주어야 한다. 
        

