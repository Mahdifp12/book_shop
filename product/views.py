from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    template_name = "product/product_list.html"
    model = Book
    context_object_name = "products"


class BookDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Book


class BookFavorite(View):
    def post(self, request):
        book_slug = request.POST['book_slug']
        book = Book.objects.get(slug=book_slug)
        request.session['book_favorite'] = book.slug

        return redirect(book.get_absolute_url())
