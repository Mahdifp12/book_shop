from django.shortcuts import render
from django.views import View
from .forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            "form": register_form
        }

        return render(request, 'book_account/register.html', context)

    def post(self, request):
        pass
