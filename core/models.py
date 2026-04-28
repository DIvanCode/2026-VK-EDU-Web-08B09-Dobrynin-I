from django.contrib.auth.models import User
from django.db import models


class ProfileManager(models.Manager):
    def best_members(self):
        return self.select_related("user").order_by("-rating", "user__username")[:5]


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="пользователь",
    )
    avatar = models.FileField(
        upload_to="avatars/", blank=True, null=True, verbose_name="аватар"
    )
    rating = models.IntegerField(default=0, verbose_name="рейтинг")

    objects = ProfileManager()

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    def __str__(self):
        return self.user.username
