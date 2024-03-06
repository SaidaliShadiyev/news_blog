from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('', views.home, name='news'),
      path('news/', views.news, name='news'),
      path('faqs/', views.faqs, name='faqs'),
      path('about/', views.about, name='about'),
]