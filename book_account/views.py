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
        register_form = RegisterForm(request.POST or None)

        if register_form.is_valid():
            print(register_form.cleaned_data)

        context = {
            "form": register_form
        }

        return render(request, 'book_account/register.html', context)