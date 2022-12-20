from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListApiBooks.as_view(), name="api-books"),
    path('<int:id>', views.book_api_view_detail, name="api-detail-book")
]