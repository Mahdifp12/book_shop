from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from jalali_date import datetime2jalali, date2jalali
from .models import Article, ArticleCategory


# Create your views here.

class ArticlesView(ListView):
    model = Article
    paginate_by = 4
    template_name = "article_module/article_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        return context


def article_categories_components(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)

    context = {
        "article_main_categories": article_main_categories
    }
    return render(request, "article_module/components/article_categories_component.html", context)
