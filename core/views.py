from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render
from application.context import get_aside_context
from .forms import LoginForm, SignupForm


def login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("questions:index")
    else:
        form = LoginForm()

    context = {
        "form": form,
        "aside": get_aside_context(),
    }
    return render(request, "core/login.html", context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect("questions:index")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("core:login")
    else:
        form = SignupForm()

    context = {
        "form": form,
        "aside": get_aside_context(),
    }
    return render(request, "core/signup.html", context)


@login_required(login_url="core:login")
def profile(request):
    user = request.user
    user_profile = getattr(user, "profile", None)
    profile_user = {
        "login": user.username,
        "email": user.email,
        "nickname": user.first_name or user.username,
        "avatar_url": user_profile.avatar.url if user_profile and user_profile.avatar else "",
        "avatar_path": user_profile.avatar.name if user_profile and user_profile.avatar else "",
    }
    context = {
        "profile_user": profile_user,
        "aside": get_aside_context(),
    }
    return render(request, "core/profile.html", context)
