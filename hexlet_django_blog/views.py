from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse

def index(request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id':50}))


def about(request):
    return render(request, 'about.html')