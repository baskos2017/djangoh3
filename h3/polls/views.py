from django.shortcuts import render

# Create your views here.

def polls_view(request):
    latest_question_list = [
        {'id': 1, 'question_text': 'У чому сенс життя?'},
        {'id': 2, 'question_text': 'Що первинне: дух чи матерія?'},
        {'id': 3, 'question_text': 'Чи існує свобода волі?'}
    ]
    return render(request, 'polls/polls_list.html', {'latest_question_list': latest_question_list})