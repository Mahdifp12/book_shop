from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Book
from site_settings.models import SiteSettings, FooterLinks, FooterLinkBox, Slider


class HomePageView(TemplateView):
    template_name = "home_module/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books: Book = Book.objects.all()
        context["slider"]: Slider = Slider.objects.filter(is_active=True)
        context["books"] = books

        return context


def site_header_component(request):
    settings: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()

    context = {
        "settings": settings
    }

    return render(
        request,
        template_name="home_base/site_header_component.html",
        context=context
    )


def site_footer_component(request):
    settings: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        "settings": settings,
        "footer_link_boxes": footer_link_boxes
    }

    return render(
        request,
        template_name="home_base/site_footer_component.html",
        context=context
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


class AboutView(TemplateView):
    template_name = "home_module/about_page.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['settings']: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        return context
