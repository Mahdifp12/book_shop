from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('cat/<str:category>', views.BookListView.as_view(), name='book-categories'),
    path('author/<str:author_name>', views.BookListView.as_view(), name='book-authors'),
    path('book-favorite', views.BookFavorite.as_view(), name='book-favorite'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('cart/', views.CartView.as_view(), name='cart-page'),
    path('add-cart/', views.AddCartView.as_view(), name='add-cart-page'),
    path('delete-from-cart/<int:pk>/', views.DeleteCartView.as_view(), name='delete-from-cart'),
]
