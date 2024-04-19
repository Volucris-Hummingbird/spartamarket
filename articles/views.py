
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.views import logout_then_login
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import HttpResponseForbidden

# from .forms import CustomUserChangeForm


@login_required
def mainpage(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return sorted_articles(request)


@login_required
def new(request):
    return render(request, "articles/new.html")


@login_required
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all().order_by("-pk")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            # 현재 로그인한 사용자를 작성자로 설정합니다.
            article.save()
            return redirect("articles:mainpage")
    else:
        form = ArticleForm()

    return render(request, "articles/new.html", {'form': form})


@login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if article.author == request.user:
            article = get_object_or_404(Article, pk=pk)
            article.delete()
    return redirect("articles:mainpage")


@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/edit.html", context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:

        # if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect("articles:detail", article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect("articles:mainpage")
    context = {
        "form": form,
        "article": article, }
    return render(request, "articles/edit.html", context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("articles:detail", article.pk)


def sorted_articles(request):
    sort_criteria = request.GET.get('sort_criteria')

    if sort_criteria == 'like_users':
        sorted_articles = Article.objects.all().order_by('-like_users__count')
    elif sort_criteria == 'views':
        sorted_articles = Article.objects.all().order_by('-views')
    elif sort_criteria == 'created_at':
        sorted_articles = Article.objects.all().order_by('-created_at')
    else:
        # 기본적으로 생성 날짜를 기준으로 정렬
        sorted_articles = Article.objects.all().order_by('-created_at')

    return render(request, 'articles/mainpage.html', {'articles': sorted_articles})


@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect("articles:detail", article.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect("articles:detail", pk)


def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) | \
        Article.objects.filter(content__icontains=query) | \
        Article.objects.filter(author__username__icontains=query)
    context = {'articles': articles}
    return render(request, 'articles/mainpage.html', context)
