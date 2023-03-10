from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Book


class HomePageView(TemplateView):
    template_name = "home_module/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books: Book = Book.objects.all()[:4]
        context["books"] = books

        return context


def site_header_component(request):
    return render(
        request,
        template_name="home_base/site_header_component.html",
        context={}
    )


def site_footer_component(request):
    return render(
        request,
        template_name="home_base/site_footer_component.html",
        context={}
    )


def site_loginform_component(request):
    return render(
        request,
        template_name="home_base/site_loginform_component.html",
        context={}
    )


def site_navbar_component(request):
    return render(
        request,
        template_name="home_base/site_navbar_component.html",
        context={}
    )
