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

def game_view(request):
    response = render(request, 'web3/web3bitcar.html')
    response["Cross-Origin-Opener-Policy"] = "same-origin"
    response["Cross-Origin-Embedder-Policy"] = "require-corp"
    response["X-Content-Type-Options"] = "nosniff"
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Cross-Origin-Embedder-Policy, Cross-Origin-Opener-Policy"
    return response