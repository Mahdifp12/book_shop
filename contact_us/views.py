from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView

from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(FormView):
    template_name = "contact_us/contact_us.html"
    form_class = ContactUsModelForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)


class CreateProfileView(CreateView):
    template_name = "contact_us/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/contact-us/profile"


class ProfileListView(ListView):
    template_name = "contact_us/profile_list.html"
    model = UserProfile
    context_object_name = "profiles"
