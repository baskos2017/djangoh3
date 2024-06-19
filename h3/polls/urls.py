from django.urls import path
from .views import polls_view

urlpatterns = [
    path('polls/', polls_view, name='polls-view'),
]
