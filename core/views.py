from django.shortcuts import render
from application.context import get_aside_context


def login(request):
    context = {
        "aside": get_aside_context(),
    }
    return render(request, "core/login.html", context)


def signup(request):
    context = {
        "aside": get_aside_context(),
    }
    return render(request, "core/signup.html", context)


def profile(request):
    profile_user = {
        "login": "dr_pepper",
        "email": "dr.pepper@mail.ru",
        "nickname": "Dr. Pepper",
        "avatar_path": "c:/avatar.jpg",
    }
    context = {
        "profile_user": profile_user,
        "aside": get_aside_context(),
    }
    return render(request, "core/profile.html", context)
