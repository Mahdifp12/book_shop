from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    # path('site-header', views.site_header_component, name="site_header"),
    # path('site-footer', views.site_footer_component, name="site_footer"),
    # path('site-loginform', views.site_loginform_component, name="site_login_form"),
    # path('site-navbar', views.site_navbar_component, name="site_navbar"),
    # path('site-head-link', views.site_head_link_component, name="site-head-link"),
    # path('site-scriptjs', views.site_script_reference, name="site-script-js"),
]
