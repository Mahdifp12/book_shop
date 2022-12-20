from django.shortcuts import render


# Create your views here.

def home_page(request):

    return render(
        request,
        template_name="home_module/index.html",
        context={}
    )


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
