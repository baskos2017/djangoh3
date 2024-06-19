from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks_view, name='tasks-view'),
    path('send-file/', send_file_view, name='send-file-view'),
    path('send-json/', send_json_view, name='send-json-view'),
    path('send-html/', send_html_view, name='send-html-view'),
    path('send-text/', send_text_view, name='send-text-view'),
]
