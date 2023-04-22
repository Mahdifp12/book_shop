from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="articles-page"),
    path('category/<str:category>', views.ArticleListView.as_view(), name="articles-by-categories-page"),
    path('<int:pk>', views.ArticleDetailView.as_view(), name="article_detail_page"),
]
