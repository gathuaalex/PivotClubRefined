from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article
