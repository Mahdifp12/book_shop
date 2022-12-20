from django.contrib import messages
from django.shortcuts import render

from .form import ContactUsForm
from .models import ContactUs


# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        obj_form = ContactUsForm(request.POST)
        if obj_form.is_valid():
            obj_contact = ContactUs(
                full_name=obj_form.cleaned_data["full_name"],
                email=obj_form.cleaned_data["email"],
                title=obj_form.cleaned_data["title"],
                message=obj_form.cleaned_data["message"],
            )

            obj_contact.save()

            messages.success(request, "پیغام شما با موفقیت ارسال شد.")

    return render(request, "contact_us/contact_us.html", context={
        "form": ContactUsForm()
    })



