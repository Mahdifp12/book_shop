from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='book-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='book-detail'),

]