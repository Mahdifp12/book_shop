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

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        self_product = self.object
        request = self.request
        is_favorite = request.session.get("book_favorite") == self_product.id
        context["is_favorite"] = is_favorite
        return context


class BookFavorite(View):
    def post(self, request):
        book_id = request.POST['book_id']
        book = Book.objects.get(pk=book_id)
        request.session['book_favorite'] = book.id

        return redirect(book.get_absolute_url())