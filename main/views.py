from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'main/home.html')
def about(request):
    return render(request, 'main/about.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'main/articles.html', {'articles': articles})
