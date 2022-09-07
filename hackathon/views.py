from django.shortcuts import render
from hackathon.utils import user_authorized_items, user_unauthorized_items, menu_items


def index(request):
    menu_context = {
        'menu_items': menu_items,
        'user_items': user_authorized_items if request.user.is_authenticated else user_unauthorized_items
    }
    menu_context.update({'title': 'ХаХатонщики', 'current_page': 'hackathon-home'})
    return render(request, 'hackathon/index.html', context=menu_context)


def team(request):
    menu_context = {
        'menu_items': menu_items,
        'user_items': user_authorized_items if request.user.is_authenticated else user_unauthorized_items,
    }
    team_members = [
        {
            'name': 'Артур Казарян',
            'task': 'Frontend, Backend',
            'photo': '/media/team/arthur.png',
            'about': 'Хочу оливье'
        },
        {
            'name': 'Дмитрий Паршин',
            'task': 'Data Science',
            'photo': '/media/team/dmitry.png',
            'about': 'Per aspera ad astra'
        },
        {
            'name': 'Никита Сидельников',
            'task': 'Data Science, Backend',
            'photo': '/media/team/nikita.png',
            'about': '123'
        },
        {
            'name': 'Ренат Шакиров',
            'task': 'Data Science, Backend',
            'photo': '/media/team/renat.png',
            'about': '123'
        }
    ]
    menu_context.update({'title': 'Команда', 'current_page': 'hackathon-team', 'team_members': team_members})
    return render(request, 'hackathon/team.html', context=menu_context)
