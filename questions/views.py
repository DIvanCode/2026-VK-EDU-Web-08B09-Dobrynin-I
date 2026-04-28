from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from application.context import get_aside_context
from .models import Answer, Question


def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get("page", 1)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def index(request):
    all_questions = Question.objects.new()
    page_obj = paginate(all_questions, request)
    context = {
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "aside": get_aside_context(),
    }
    return render(request, "questions/index.html", context)


def hot(request):
    all_questions = Question.objects.hot()
    page_obj = paginate(all_questions, request)
    context = {
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "aside": get_aside_context(),
    }
    return render(request, "questions/hot.html", context)


def tag(request, tag_name):
    all_questions = Question.objects.by_tag(tag_name)
    page_obj = paginate(all_questions, request)
    context = {
        "tag_name": tag_name,
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "aside": get_aside_context(),
    }
    return render(request, "questions/tag.html", context)


def question(request, question_id):
    question_item = get_object_or_404(Question.objects.with_counters(), id=question_id)
    all_answers = Answer.objects.for_question(question_id)
    page_obj = paginate(all_answers, request)
    context = {
        "question_id": question_id,
        "question_item": question_item,
        "answers": page_obj.object_list,
        "page_obj": page_obj,
        "aside": get_aside_context(),
    }
    return render(request, "questions/question.html", context)


def ask(request):
    context = {
        "aside": get_aside_context(),
    }
    return render(request, "questions/ask.html", context)
