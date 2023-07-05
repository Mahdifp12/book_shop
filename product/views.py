from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, BookCategory


class BookListView(ListView):
    template_name = "product/product_list.html"
    model = Book
    context_object_name = "products"
    ordering = ['-price']
    paginate_by = 5


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


def book_categories_components(request: HttpRequest):
    book_categories = BookCategory.objects.prefetch_related('bookcategories_set') \
        .filter(is_active=True, parent_id=None)

    return render(request, template_name="product/components/product_categories_component.html")