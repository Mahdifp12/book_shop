from django.shortcuts import render, get_object_or_404

from .models import Book


def product_list(request):
    list_of_product = Book.objects.all().order_by('-price')[:5]
    return render(request, 'product/product_list.html', {
        "products": list_of_product

    }
                  )


def product_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "product/product_detail.html", {
        "book": book,
    })
