from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


# Create your views here.

class ArticlesView(ListView):
    model = Article
    paginate_by = 4
    template_name = "article_module/article_page.html"
