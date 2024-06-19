from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse

# Create your views here.

lets_do_it = [
    {'priority': 100, 'task': 'Скласти перелік справ'},
    {'priority': 150, 'task': 'Вивчати Django'},
    {'priority': 1, 'task': 'Подумати про сенс життя'}
]

def tasks_view(request):
    context = {'tasks': lets_do_it}
    sorted_tasks = sorted(lets_do_it, key=lambda x: x['priority'], reverse=True)
    return render(request, 'task1/tasks.html', {'tasks': sorted_tasks})

def send_file_view(request):
    content = "Ось ваш файл"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    response.status_code = 227
    return response

def send_json_view(request):
    data = {
        'message': 'Це JSON-відповідь',
        'status': 'success'
    }
    return JsonResponse(data)

def send_html_view(request):
    context={
        'title': 'HTML Відповідь', 'message': 'Це HTML-відповідь'
        }
    return render(request, 'task1/sample.html', context=context)

def send_text_view(request):
    return HttpResponse("Це текстова відповідь", content_type='text/plain')


