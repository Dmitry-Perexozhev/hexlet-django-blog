from django.shortcuts import render

def article(request):
    return render(request, 'article.html', context={'tags':1})
