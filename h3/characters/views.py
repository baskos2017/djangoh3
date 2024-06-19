from django.shortcuts import render

# Create your views here.

def characters_view(request):
    characters = [
        {'name': 'Шаддам IV', 'surname': 'Корріно'},
        {'name': 'Пол', 'surname': 'Атрейдес'},
        {'name': 'Франклін', 'surname': 'Герберт'}
    ]
    return render(request, 'characters/characters_list.html', {'characters': characters})