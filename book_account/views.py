from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, LoginForm
from .models import User
from django.utils.crypto import get_random_string


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

    def post(self, request):
        pass


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
