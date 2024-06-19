from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'task2/home.html')

def luke_view(request):
    return render(request, 'task2/luke.html')

def leia_view(request):
    return render(request, 'task2/leia.html')

def han_view(request):
    return render(request, 'task2/han.html')