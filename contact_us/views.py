from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import ContactUsModelForm


class ContactUsView(View):
    def get(self, request):
        form = ContactUsModelForm()

        return render(
            request,
            template_name="contact_us/contact_us.html",
            context={
                "form": form
            }
        )

    def post(self, request):
        data = request.POST
        form = ContactUsModelForm(data=data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home-page'))

        form = ContactUsModelForm()

        return render(
            request,
            template_name="contact_us/contact_us.html",
            context={
                "form": form
            }
        )
