from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
      return HttpResponse('kboog')

def index(request):
      news_list = News.objects.all()
      context = {
            'news_list': news_list
      }
      return render(request, 'blog/homepage.html', context)

def news(request):
      news = News.objects.all().order_by('?')
      context = {
            'news': news
      }
      return render(request, 'blog/news.html', context)

def faqs(request):
      return render(request, 'blog/faqs.html')

def about(request):
      return render(request, 'blog/about.html')