from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from book_account.models import User
from .forms import EditProfileModelForm, ChangePasswordForm


# Create your views here.

class UserPanelDashboardPage(TemplateView):
    template_name = "user_panel_module/user_panel_page.html"


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            "form": edit_form,
            "current_user": current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            "form": edit_form,
            "current_user": current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        context = {
            "form": form
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user = User.objects.filter(id=request.user.id).first()
            current_password = form.cleaned_data.get("current_password")
            is_correct_password = current_user.check_password(current_password)

            if is_correct_password:
                new_password = form.cleaned_data.get("password")
                current_user.set_password(new_password)
                current_user.save()
                logout(request)
                return redirect(reverse("login-page"))
            else:
                form.add_error('password', 'رمز عبور وارد شده اشتباه میباشد')
        context = {
            "form": form
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


def user_panel_menu_component(request: HttpRequest):
    return render(request, "components/user_panel_menu_component.html")
