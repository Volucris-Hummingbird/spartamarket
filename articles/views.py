
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.views import logout_then_login
from .models import Article
from .forms import ArticleForm


def mainpage(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/mainpage.html", context)

def new(request):
    return render(request, "articles/new.html")

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("articles:mainpage")
    else:
        form = ArticleForm()

    return redirect('articles:mainpage')

