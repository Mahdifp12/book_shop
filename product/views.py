from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, BookCategory, BookAuthor


class BookListView(ListView):
    template_name = "product/product_list.html"
    model = Book
    context_object_name = "products"
    ordering = ['-price']
    paginate_by = 5

    def get_queryset(self):
        query = super(BookListView, self).get_queryset()
        query2 = super(BookListView, self).get_queryset()
        query = query.filter(is_active=True)
        query2 = query2.filter(is_active=True)
        category_name = self.kwargs.get("category")
        author_name = self.kwargs.get("authorname")
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if author_name is not None:
            query2 = query2.filter(author__url_name__iexact=author_name)

            return query2

        return query


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
    book_categories = BookCategory.objects.prefetch_related('bookcategory_set') \
        .filter(is_active=True, parent_id=None)

    context = {
        'book_categories': book_categories
    }

    return render(request, template_name="product/components/product_categories_component.html", context=context)


def book_authors_components(request: HttpRequest):
    book_authors = BookAuthor.objects.filter(is_active=True, is_delete=False)

    context = {
        'book_authors': book_authors
    }

    return render(request, "product/components/product_authors_components.html", context)
