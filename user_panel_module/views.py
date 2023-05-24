from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .forms import EditProfileModelForm


# Create your views here.

class UserPanelDashboardPage(TemplateView):
    template_name = "user_panel_module/user_panel_page.html"


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        edit_form = EditProfileModelForm()
        context = {
            "form": edit_form,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        return render(request, 'user_panel_module/edit_profile_page.html', {})


def user_panel_menu_component(request: HttpRequest):
    return render(request, "components/user_panel_menu_component.html")
