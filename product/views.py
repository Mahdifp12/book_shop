from django.views.generic import ListView, DetailView
from .models import Book


class ProductListView(ListView):
    template_name = "product/product_list.html"
    model = Book
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Book
