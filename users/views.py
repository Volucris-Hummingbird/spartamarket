from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from articles.models import Article
from articles.models import ArticleLike


def profile(request, user):
    member = get_object_or_404(get_user_model(), username=user)

    follower_count = member.followers.count()
    following_count = member.following.count()
    liked_articles = Article.objects.filter(like_users=member)

    context = {
        "member": member,
        "follower_count": follower_count,
        "following_count": following_count,
        "liked_articles": liked_articles,
    }

    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
