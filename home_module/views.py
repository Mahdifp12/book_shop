from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home_module/index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


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
