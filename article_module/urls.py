from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name="articles-page"),
    path('category/<str:category>', views.ArticlesView.as_view(), name="articles-by-categories-page"),
]
