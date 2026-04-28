from core.models import Profile
from questions.models import Tag


def get_aside_context():
    popular_tags = Tag.objects.popular()
    best_members = Profile.objects.best_members()
    return {
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
