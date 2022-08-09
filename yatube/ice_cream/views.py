from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница


def index(request):
    template = 'ice_cream/index.html'
    return render(request, template)


# Страница со списком мороженого
def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
