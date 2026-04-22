from django.db import models
from django.db.models import Count, IntegerField, OuterRef, Q, Subquery, Sum, Value
from django.db.models.functions import Coalesce

from core.models import Profile


class TagManager(models.Manager):
    def popular(self):
        return self.annotate(questions_count=Count("questions")).order_by(
            "-questions_count", "name"
        )[:8]


class QuestionManager(models.Manager):
    def with_counters(self):
        likes_score = (
            Like.objects.filter(question=OuterRef("pk"))
            .values("question")
            .annotate(total=Sum("value"))
            .values("total")
        )
        return self.prefetch_related("tags").select_related("author__user").annotate(
            score=Coalesce(Subquery(likes_score), Value(0), output_field=IntegerField()),
            answers_count=Count("answers", distinct=True),
        )

    def new(self):
        return self.with_counters().order_by("-created_at")

    def hot(self):
        return self.with_counters().order_by("-score", "-created_at")

    def by_tag(self, tag_slug):
        return self.with_counters().filter(tags__slug=tag_slug).order_by("-created_at")


class AnswerManager(models.Manager):
    def for_question(self, question_id):
        return (
            self.select_related("author__user")
            .filter(question_id=question_id)
            .annotate(score=Sum("likes__value", default=0))
            .order_by("-is_correct", "-score", "created_at")
        )


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="название")
    slug = models.SlugField(max_length=64, unique=True, verbose_name="slug")

    objects = TagManager()

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст")
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="автор",
    )
    tags = models.ManyToManyField(
        Tag, related_name="questions", blank=True, verbose_name="теги"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    objects = QuestionManager()

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="вопрос",
    )
    text = models.TextField(verbose_name="текст")
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="автор",
    )
    is_correct = models.BooleanField(default=False, verbose_name="правильный ответ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    objects = AnswerManager()

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    def __str__(self):
        return self.text[:50]


class Like(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTE_CHOICES = (
        (LIKE, "лайк"),
        (DISLIKE, "дизлайк"),
    )

    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="likes", verbose_name="автор"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="likes",
        blank=True,
        null=True,
        verbose_name="вопрос",
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name="likes",
        blank=True,
        null=True,
        verbose_name="ответ",
    )
    value = models.SmallIntegerField(choices=VOTE_CHOICES, verbose_name="оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "лайки"
        constraints = [
            models.CheckConstraint(
                check=(
                    Q(question__isnull=False, answer__isnull=True)
                    | Q(question__isnull=True, answer__isnull=False)
                ),
                name="like_has_one_target",
            ),
            models.UniqueConstraint(
                fields=["author", "question"], name="unique_question_like"
            ),
            models.UniqueConstraint(fields=["author", "answer"], name="unique_answer_like"),
        ]

    def __str__(self):
        target = self.question or self.answer
        return f"{self.author} -> {target}: {self.value}"
