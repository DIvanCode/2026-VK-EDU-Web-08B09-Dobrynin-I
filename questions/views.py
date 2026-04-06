from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
    all_questions = []
    for i in range(1, 31):
        all_questions.append(
            {
                "id": i,
                "title": "How to build a moon park ?",
                "text": "Guys, i have trouble with a moon park.\nCan't find th black-jack...",
                "score": 5,
                "answers_count": 3,
                "asked_at": "17.03.2026 20:00",
                "tags": [
                    {"name": "black-jack", "slug": "black-jack"},
                    {"name": "bender", "slug": "bender"},
                ],
            }
        )
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
    page_obj = paginate(all_questions, request)
    context = {
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "questions/index.html", context)


def hot(request):
    all_questions = []
    for i in range(1, 11):
        all_questions.append(
            {
                "id": i,
                "title": "How to build a moon park ?",
                "text": "Guys, i have trouble with a moon park.\nCan't find th black-jack...",
                "score": 20 - i,
                "answers_count": 3,
                "asked_at": "17.03.2026 20:00",
                "tags": [
                    {"name": "black-jack", "slug": "black-jack"},
                    {"name": "bender", "slug": "bender"},
                ],
            }
        )
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
    page_obj = paginate(all_questions, request)
    context = {
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "questions/hot.html", context)


def tag(request, tag_name):
    all_questions = []
    for i in range(1, 31):
        all_questions.append(
            {
                "id": i,
                "title": "How to build a moon park ?",
                "text": "Guys, i have trouble with a moon park.\nCan't find th black-jack...",
                "score": 5,
                "answers_count": 3,
                "asked_at": "17.03.2026 20:00",
                "tags": [
                    {"name": "black-jack", "slug": "black-jack"},
                    {"name": "bender", "slug": "bender"},
                ],
            }
        )
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
    page_obj = paginate(all_questions, request)
    context = {
        "tag_name": tag_name,
        "questions": page_obj.object_list,
        "page_obj": page_obj,
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "questions/tag.html", context)


def question(request, question_id):
    question_item = {
        "id": question_id,
        "title": "How to build a moon park ?",
        "text": "Lorem ipsum &mdash; dolor sit amet, consectetuler adipisicing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.",
        "score": 5,
        "answers_count": 3,
        "asked_at": "17.03.2026 20:00",
        "tags": [
            {"name": "black-jack", "slug": "black-jack"},
            {"name": "bender", "slug": "bender"},
        ],
    }
    all_answers = [
        {
            "id": 1,
            "text": "First of all I would like to thank you for the invitation to participate in such a ... Russia is the huge territory which in many respects needs to be render habitable.",
            "score": 5,
            "answered_at": "17.03.2026 20:00",
            "is_correct": True,
        },
        {
            "id": 2,
            "text": "First of all I would like to thank you for the invitation to participate in such a ... Russia is the huge territory which in many respects needs to be render habitable.",
            "score": 3,
            "answered_at": "17.03.2026 20:00",
            "is_correct": False,
        },
    ]
    page_obj = paginate(all_answers, request)
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
        "question_id": question_id,
        "question_item": question_item,
        "answers": page_obj.object_list,
        "page_obj": page_obj,
        "popular_tags": popular_tags,
        "best_members": best_members,
    }
    return render(request, "questions/question.html", context)


def ask(request):
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
    return render(request, "questions/ask.html", context)
