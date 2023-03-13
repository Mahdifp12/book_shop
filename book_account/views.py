from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            "form": register_form
        }

        return render(request, 'book_account/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST or None)

        if register_form.is_valid():
            user_email = register_form.cleaned_data.get("email")
            user_password = register_form.cleaned_data.get("password")

            user: bool = User.objects.filter(email__iexact=user_email).exists()

            if user:
                register_form.add_error("email", "ایمیل وارد شده تکراری میباشد")

            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(length=72),
                    is_active=False,
                    username=user_email
                )
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code

                return redirect(reverse("login-page"))

        context = {
            "form": register_form
        }

        return render(request, 'book_account/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()

        context = {
            "form": login_form
        }

        return render(request, 'book_account/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get("email")
            user_password = login_form.cleaned_data.get("password")
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error(field="email", error="حساب کاربری شما فعال نشده است")

                else:
                    is_correct_password = user.check_password(user_password)
                    if is_correct_password:
                        login(request, user)
                        return redirect(reverse("home-page"))
                    else:
                        login_form.add_error(field="email", error="حساب کاربری شما یافت نشد")
            else:
                login_form.add_error(field="email", error="حساب کاربری شما یافت نشد")

        context = {
            "form": login_form
        }

        return render(request, "book_account/login.html", context)


class ActivateAccount(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()

        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(length=72)
                user.save()

                return redirect(reverse("login-page"))

            else:
                # Todo : This is here your was activated account message
                pass

        raise Http404()

    def post(self, request):
        pass


class ForgetPassword(View):
    def get(self, request: HttpRequest):
        forget_password_form = ForgetPasswordForm()

        context = {
            "form": forget_password_form
        }
        return render(request, 'book_account/forget_password.html', context)

    def post(self, request: HttpRequest):
        forget_password_form = ForgetPasswordForm(request.POST)
        if forget_password_form.is_valid():
            user_email = forget_password_form.cleaned_data.get("email")
            user: User = User.objects.filter(email__iexact=user_email).first()

            if user is not None:
                # Todo : i'm must add send email system for reset password user
                pass

        context = {
            "form": forget_password_form
        }

        return render(request, "book_account/forget_password.html", context)


class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()

        if user is None:
            return redirect(reverse("login-page"))

        reset_password_form = ResetPasswordForm()

        context = {
            "form": reset_password_form,
            "user": user
        }

        return render(request, "book_account/reset_password.html", context)

    def post(self, request: HttpRequest, active_code):
        reset_password_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()

        if reset_password_form.is_valid():
            if user is None:
                return redirect(reverse("login-page"))

            user_new_pass = reset_password_form.cleaned_data.get("password")
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()

            return redirect(reverse("login-page"))

        context = {
            "form": reset_password_form,
            "user": user
        }

        return render(request, "book_account/reset_password.html", context)
