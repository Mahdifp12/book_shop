from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactUsForm
from .models import ContactUs


# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        obj_form = ContactUsForm(data=request.POST)
        if obj_form.is_valid():
            obj_contact = ContactUs(
                full_name=obj_form.cleaned_data["full_name"],
                email=obj_form.cleaned_data["email"],
                title=obj_form.cleaned_data["title"],
                message=obj_form.cleaned_data["message"],
            )

            obj_contact.save()
            return HttpResponseRedirect(reverse('home-page'))

    form = ContactUsForm()
    return render(request, "contact_us/contact_us.html", context={
        "form": form
    })
