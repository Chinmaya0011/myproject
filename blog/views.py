# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hey Chinmaya")

def success(request):
    peoples = [
        {'name': "Chinmaya", 'age': 25},
        {'name': "John", 'age': 30},
        {'name': "Ayesha", 'age': 28},
        {'name': "Raj", 'age': 35},
        {'name': "Sophia", 'age': 2},
        {'name': "Michael", 'age': 27}
    ]
    return render(request, 'blog/index.html', context={'peoples': peoples})  # Make sure to include the path based on the folder structure

def chinmaya(request):
    return HttpResponse("<h1>Chinmaya Kumar Mishra</h1>")
