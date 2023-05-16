from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article_module.models import Article, ArticleCategory, ArticleComment


# Create your views here.

class ArticleListView(ListView):
    model = Article
    paginate_by = 4
    template_name = "article_module/article_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get("category")
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_module/article_detail_page.html"

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)

        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments']: ArticleComment = ArticleComment.objects.filter(article_id=article.id, parent=None) \
            .order_by("-create_date")\
            .prefetch_related("articlecomment_set")
        context['comments_count']: ArticleComment = ArticleComment.objects.filter(article_id=article.id).count()
        return context


def article_categories_components(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)

    context = {
        "article_main_categories": article_main_categories
    }
    return render(request, "article_module/components/article_categories_component.html", context)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_comment = request.GET.get("article_comment")
        article_id = request.GET.get("article_id")
        parent_id = request.GET.get("parent_id")
        print(article_comment, article_id, parent_id)

        new_comment: ArticleComment = ArticleComment(
            text=article_comment,
            article_id=article_id,
            parent_id=parent_id,
            user_id=request.user.id,
        )

        new_comment.save()

        context = {
            'comments': ArticleComment.objects.filter(article_id=article_id, parent=None).order_by('-create_date') \
                .prefetch_related("articlecomment_set"),

            'comments_count': ArticleComment.objects.filter(article_id=article_id).count()
        }

        return render(request, 'article_module/includes/article_comment_partial.html', context)

    return HttpResponse("This is response text")
