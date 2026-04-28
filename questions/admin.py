from django.contrib import admin

from .models import Answer, Like, Question, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("tags", "created_at")
    search_fields = ("title", "text")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "author", "is_correct", "created_at")
    list_filter = ("is_correct", "created_at")
    search_fields = ("text",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("author", "question", "answer", "value", "created_at")
    list_filter = ("value", "created_at")
