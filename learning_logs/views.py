from django.shortcuts import render

# Create your views here.


def index(request):
    """Learning Log app's homepage"""
    return render(request, 'learning_logs/index.html')
