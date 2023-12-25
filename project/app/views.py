from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    return HttpResponse('<h1>Main Page</h2>'
                        f'<h2>Login: {login}, Password: {password}')


def pop_post(request):
    return HttpResponse(f'Пост 1')


def last_post(request):
    return HttpResponse(f'Пост 2')


def posts(request):
    return HttpResponse(f'Пост 3')


def likes(request, id):
    return HttpResponse(f'Лайк к посту: {id}')


def comm(request, id):
    return HttpResponse(f'Комментарий к посту: {id}')


def about(request):
    return HttpResponseRedirect('/admin')


def contacts(request):
    return HttpResponsePermanentRedirect('/')


def err(request, id):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')


def access(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    if login == 'admin' and password == 'admin':
        return HttpResponse('Всё норм')
    else:
        return HttpResponseBadRequest('Чё-то не то :/')


def json(request):
    return JsonResponse({'name': 'Nazar', 'age': 16})


def set(request):
    name = request.GET.get('name', 'Undefined')
    response = HttpResponse(f'Hello {name}')
    response.set_cookie('name', name)
    return response


def get(request):
    name = request.COOKIES['name']
    return HttpResponse(f'Hello {name}')