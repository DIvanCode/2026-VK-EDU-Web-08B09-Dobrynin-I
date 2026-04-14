def get_aside_context():
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
    return {
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
