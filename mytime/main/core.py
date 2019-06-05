from .models import Task, List
from datetime import datetime, timedelta


SMART_LISTS = {'inbox', 'today', 'tomorrow', 'week', 'starred', 'all'}


def get_filled_lists(user):
    context = {}

    personal_lists = List.objects.filter(user=user)
    context['personal_lists'] = list(personal_lists.values())

    for list_item, context_list_item in zip(personal_lists, context['personal_lists']):
        context_list_item['count_tasks'] = list_item.count_tasks()
        context_list_item['count_overdue_tasks'] = list_item.count_overdue_tasks()

    all_tasks = Task.objects.filter(user=user)
    now = datetime.now().date()
    overdue_tasks = all_tasks.filter(planned_on__date__lt=now)
    count_overdue_tasks = overdue_tasks.count()

    inbox = all_tasks.filter(list=None)
    today = all_tasks.filter(planned_on__date=now) | overdue_tasks
    tomorrow = all_tasks.filter(planned_on__date=now + timedelta(days=1))
    week = all_tasks.filter(planned_on__date__gte=now, planned_on__date__lte=now + timedelta(days=7)) | overdue_tasks
    starred = all_tasks.filter(starred=True)

    smart_lists = {
        'inbox':{
            'name': 'Входящие',
            'slug': 'inbox',
            'tasks': list(inbox.values()),
            'count_tasks': inbox.count(),
            'count_overdue_tasks': inbox.filter(planned_on__date__lt=now).count(),
        },
        'today':{
            'name': 'Сегодня',
            'slug': 'today',
            'tasks': list(today.values()),
            'count_tasks': today.count(),
            'count_overdue_tasks': count_overdue_tasks},
        'tomorrow':{
            'name': 'Завтра',
            'slug': 'tomorrow',
            'tasks': list(tomorrow.values()),
            'count_tasks': tomorrow.count(),
            'count_overdue_tasks': 0,
        },
        'week':{
            'name': 'Неделя',
            'slug': 'week',
            'tasks': list(week.values()),
            'count_tasks': week.count(),
            'count_overdue_tasks': count_overdue_tasks,
        },
        'starred':{
            'name': 'Отмеченные',
            'slug': 'starred',
            'tasks': list(starred.values()),
            'count_tasks': starred.count(),
            'count_overdue_tasks': starred.filter(planned_on__date__lt=now).count(),
        },
        'all':{
            'name': 'Все',
            'slug': 'all',
            'tasks': list(all_tasks.values()),
            'count_tasks': all_tasks.count(),
            'count_overdue_tasks': count_overdue_tasks,
        },

    }

    context['smart_lists'] = smart_lists
    return context


def make_task(request):
    user = request.user
    list_id = request.POST.get('active_list_id')
    title = request.POST.get('title')
    starred = bool(request.POST.get('starred'))
    planned_on = request.POST.get('planned_on')

    if list_id not in SMART_LISTS:
        task_list = List.objects.get(pk=int(list_id))
        task = Task.objects.create(user=user, list=task_list, title=title,
                                   starred=starred, planned_on=datetime.now()) # временно datetime.now()
    else:
        options = {
            'inbox': {
                'user': user,
                'title': title,
                'starred': starred,
                'planned_on':datetime.now() # временно datetime.now()
            },
            'today': {
                'user': user,
                'title': title,
                'starred': starred,
                'planned_on': datetime.now()
            },
            'tomorrow': {
                'user': user,
                'title': title,
                'starred': starred,
                'planned_on': datetime.now() + timedelta(days=1)  # временно datetime.now()
            },
            'starred': {
                'user': user,
                'title': title,
                'starred': True,
                'planned_on': datetime.now() # временно datetime.now()
            },
            'all': {
                'user': user,
                'title': title,
                'starred': starred,
                'planned_on': datetime.now()  # временно datetime.now()
            }
        }

        task = Task.objects.create(**options[list_id])

    return task
