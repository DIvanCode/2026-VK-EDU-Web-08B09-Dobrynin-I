from django.shortcuts import render


def login(request):
    popular_tags = [
        {"name": "perl", "slug": "perl"},
        {"name": "python", "slug": "python"},
        {"name": "TechnoPark", "slug": "technopark"},
        {"name": "MySQL", "slug": "mysql"},
        {"name": "django", "slug": "django"},
        {"name": "Mail.Ru", "slug": "mail-ru"},
        {"name": "Voloshin", "slug": "voloshin"},
        {"name": "Firefox", "slug": "firefox"},
    ]
    best_members = ["Mr. Freeman", "Dr. House", "Bender", "Queen Victoria", "V. Pupkin"]
    context = {
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "core/login.html", context)


def signup(request):
    popular_tags = [
        {"name": "perl", "slug": "perl"},
        {"name": "python", "slug": "python"},
        {"name": "TechnoPark", "slug": "technopark"},
        {"name": "MySQL", "slug": "mysql"},
        {"name": "django", "slug": "django"},
        {"name": "Mail.Ru", "slug": "mail-ru"},
        {"name": "Voloshin", "slug": "voloshin"},
        {"name": "Firefox", "slug": "firefox"},
    ]
    best_members = ["Mr. Freeman", "Dr. House", "Bender", "Queen Victoria", "V. Pupkin"]
    context = {
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "core/signup.html", context)


def profile(request):
    profile_user = {
        "login": "dr_pepper",
        "email": "dr.pepper@mail.ru",
        "nickname": "Dr. Pepper",
        "avatar_path": "c:/avatar.jpg",
    }
    popular_tags = [
        {"name": "perl", "slug": "perl"},
        {"name": "python", "slug": "python"},
        {"name": "TechnoPark", "slug": "technopark"},
        {"name": "MySQL", "slug": "mysql"},
        {"name": "django", "slug": "django"},
        {"name": "Mail.Ru", "slug": "mail-ru"},
        {"name": "Voloshin", "slug": "voloshin"},
        {"name": "Firefox", "slug": "firefox"},
    ]
    best_members = ["Mr. Freeman", "Dr. House", "Bender", "Queen Victoria", "V. Pupkin"]
    context = {
        "profile_user": profile_user,
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "core/profile.html", context)
