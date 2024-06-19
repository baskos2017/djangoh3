from django.urls import path
from .views import home_view, luke_view, leia_view, han_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('luke/', luke_view, name='luke-view'),
    path('leia/', leia_view, name='leia-view'),
    path('han/', han_view, name='han-view'),
]
