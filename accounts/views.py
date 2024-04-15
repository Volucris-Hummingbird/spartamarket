

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# 로그인 - 첫 화면
def login(request):
    return render(request, "accounts/login.html")

# 회원가입
def signup(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # auth_login(request, user)
    #         return redirect("login")
    #     else:
    #         form = UserCreationForm()
    #     context = {"form" : form}
    return render(request, "accounts/signup.html")

