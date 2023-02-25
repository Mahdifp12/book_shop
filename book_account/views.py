from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm
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
        login_form = None

        context = {
            "form": None
        }

        return render(request, 'book_account/register.html', context)

    def post(self, request):
        pass
