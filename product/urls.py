from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('cat/<str:category>', views.BookListView.as_view(), name='book-categories'),
    path('book-favorite', views.BookFavorite.as_view(), name='book-favorite'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),

]
