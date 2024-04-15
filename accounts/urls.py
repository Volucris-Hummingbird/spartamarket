from django.urls import path
from django import forms
from . import views


app_name = "accounts"

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20)
    content=forms.CharField()
    
    
    

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]
