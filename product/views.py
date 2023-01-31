from django.views.generic import ListView, DetailView
from .models import Book


class ProductListView(ListView):
    template_name = "product/product_list.html"
    model = Book
    context_object_name = "products"


class ProductDetailView(DetailView):
    pass

#
# def product_detail(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     return render(request, "product/product_detail.html", {
#         "book": book,
#     })
