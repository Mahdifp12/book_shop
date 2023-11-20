from django.contrib import messages
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import QuantityForm
from .models import Book, BookCategory, BookAuthor, Cart


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
        author_name = self.kwargs.get("author_name")
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


class CartView(View):
    template_name = "product/cart_page.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        total_quantity = sum(item.book.price * item.quantity for item in cart_items)

        context = {
            "cart_items": cart_items,
            "total_quantity": total_quantity
        }

        return render(request, self.template_name, context)


class AddCartView(View):
    def get(self, request: HttpRequest):
        form = QuantityForm()

        context = {
            'form': form
        }

        return render(request, "product/product_detail.html", context)

    def post(self, request: HttpRequest):
        book_id = request.POST.get("book_id")
        if book_id and request.user.is_authenticated:
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                return HttpResponseBadRequest("کتاب یافت نشد")

            user = request.user
            # quantity = form.cleaned_data['quantity']
            try:
                cart_item = Cart.objects.get(user=user, book=book)
            except Cart.DoesNotExist:
                cart_item = Cart(user=user, book=book)
                cart_item.save()
            else:
                cart_item.quantity += 1
                cart_item.save()
        else:
            return redirect(reverse("register-page"))

        messages.success(request, "کتاب با موفقیت به سبد خرید شما اضافه شد.")

        return redirect(reverse("cart-page"))


class DeleteCartView(UserPassesTestMixin, DeleteView):  # in future
    model = Cart
    template_name = "product/cart_page.html"
    success_url = reverse_lazy("cart-page")
    context_object_name = "item"
    raise_exception = True

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


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
