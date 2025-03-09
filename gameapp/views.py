from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def game(request):
    return render(request, 'gameapp/game.html')

def blog(request):
    return render(request, 'gameapp/blog.html')

def news(request):
    return render(request, 'gameapp/news.html')

def roadmap(request):
    return render(request, 'gameapp/roadmap.html')

def radingame(request):
    return render(request, 'gameapp/rating.html')

