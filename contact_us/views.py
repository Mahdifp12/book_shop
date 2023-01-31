from django.views.generic.edit import FormView

from .forms import ContactUsModelForm


class ContactUsView(FormView):
    template_name = "contact_us/contact_us.html"
    form_class = ContactUsModelForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)
