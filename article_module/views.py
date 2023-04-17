from django.shortcuts import render
from django.views.generic import ListView
from jalali_date import datetime2jalali, date2jalali
from .models import Article


# Create your views here.

class ArticlesView(ListView):
    model = Article
    paginate_by = 4
    template_name = "article_module/article_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        context['date'] = date2jalali(self.request.user.date_joined)
        return context
