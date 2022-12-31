from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=100,
                                label="نام شما",
                                error_messages={
                                    "required": "لطفا نام خود را وارد کنید",
                                    "max_length": "تعداد حروف نام شما بالاتر از حد مجاز است"
                                },
                                widget=forms.TextInput(attrs={
                                    "class": "form-group",
                                    "placeholder": "نام شما"
                                })
                                )
    email = forms.EmailField(max_length=200,
                             label="ایمیل شما",
                             error_messages={
                                 "required": "لطفا ایمیل خود را وارد کنید"
                             },
                             widget=forms.EmailInput(attrs={
                                 "class": "form-group",
                                 "placeholder": "ایمیل شما"
                             }
                             )
                             )
    title = forms.CharField(max_length=200,
                            label="عنوان پیغام شما",
                            widget=forms.TextInput(attrs={
                                "class": "form-group",
                                "placeholder": "عنوان پیغام شما"
                            })
                            )
    message = forms.CharField(label="پیغام شما",
                              widget=forms.Textarea(attrs={
                                  "class": "form-group",
                                  "placeholder": "پیغام شما"
                              })
                              )
