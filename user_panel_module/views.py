from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class UserPanelDashboardPage(TemplateView):
    template_name = "user_panel_module/user_panel_page.html"
