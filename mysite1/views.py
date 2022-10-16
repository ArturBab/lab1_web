from django.shortcuts import render, redirect
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')


processors_list = [
    {
    'id':0,
    'name': 'AMD',
    'text': '''AMD Ze best!!!'''
    },
    {
     'id': 1,
     'name': 'INTEL',
     'text': '''NO!!!'''
    }
]

graphic_cards_list = [
    {
        'id': 0,
        'name': 'NVIDIA',
        'text': '''Ну норм видюхи'''
    },
    {
        'id': 1,
        'name': 'AMD',
        'text': '''Хорошие видюхи'''
    },
    {
        'id': 2,
        'name': 'INTEL',
        'text': '''Bruh'''
    },
]

def processors(request):
    return render(request, 'processors.html', {
        'processors': processors_list
    })

def graphic_cards(request):
    return render(request, 'graphic_cards.html', {
        'graphic_cards': graphic_cards_list
    })


def catalog_processors(request, number):
    if number < len(processors_list):
        return render(request, 'catalog_processors.html', processors_list[number])
    else:
        return redirect('/')

def catalog_graphic_cards(request, number):
     if number < len(graphic_cards_list):
        return render(request, 'catalog_processors.html', graphic_cards_list[number])
     else:
         return redirect('/')


# Create your views here.
