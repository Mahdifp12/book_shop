from django import forms
from .models import ContactUs


# class ContactUsForm(forms.Form):
#     full_name = forms.CharField(max_length=100,
#                                 label="نام شما",
#                                 error_messages={
#                                     "required": "لطفا نام خود را وارد کنید",
#                                     "max_length": "تعداد حروف نام شما بالاتر از حد مجاز است"
#                                 },
#                                 widget=forms.TextInput(attrs={
#                                     "class": "form-group",
#                                     "placeholder": "نام شما"
#                                 })
#                                 )
#     email = forms.EmailField(max_length=200,
#                              label="ایمیل شما",
#                              error_messages={
#                                  "required": "لطفا ایمیل خود را وارد کنید"
#                              },
#                              widget=forms.EmailInput(attrs={
#                                  "class": "form-group",
#                                  "placeholder": "ایمیل شما"
#                              }
#                              )
#                              )
#     title = forms.CharField(max_length=200,
#                             label="عنوان پیغام شما",
#                             widget=forms.TextInput(attrs={
#                                 "class": "form-group",
#                                 "placeholder": "عنوان پیغام شما"
#                             })
#                             )
#     message = forms.CharField(label="پیغام شما",
#                               widget=forms.Textarea(attrs={
#                                   "class": "form-group",
#                                   "placeholder": "پیغام شما"
#                               })
#                               )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'full_name',
            'email',
            'title',
            'message'
        ]
        labels = {
            'full_name': 'نام شما',
            'email': 'ایمیل شما',
            'title': 'عنوان پیغام شما',
            'message': 'پیغام شما',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                "class": "form-group",
                "placeholder": "نام شما"
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-group",
                "placeholder": "ایمیل شما"
            }),
            'title': forms.TextInput(attrs={
                "class": "form-group",
                "placeholder": "عنوان پیغام شما"
            }),
            'message': forms.Textarea(attrs={
                "class": "form-group",
                "placeholder": "پیغام شما"
            })
        }

        error_messages = {
            'full_name': {
                "required": "لطفا نام خود را وارد کنید",
                "max_length": "تعداد حروف نام شما بالاتر از حد مجاز است"
            },
            'email': {
                "required": "لطفا ایمیل خود را وارد کنید"
            },
            'title': {
                "required": "لطفا عنوان پیغام خود را وارد کنید"
            },
            'message': {
                "required": "لطفا پیغام خود را وارد کنید"
            }
        }
