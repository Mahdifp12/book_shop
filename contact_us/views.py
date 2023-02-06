from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views import View
from .forms import ContactUsModelForm, ProfileForm
from .models import UserProfile


class ContactUsView(FormView):
    template_name = "contact_us/contact_us.html"
    form_class = ContactUsModelForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, template_name="contact_us/create_profile.html", context={
            "form": form
        })

    def post(self, request):
        form_submit = ProfileForm(request.POST, request.FILES)

        if form_submit.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()

            return HttpResponseRedirect(reverse("create-profile-page"))

        return render(request, template_name="contact_us/create_profile.html", context={
            "form": form_submit
        })
