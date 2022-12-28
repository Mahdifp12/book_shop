from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=200, label="نام شما", error_messages={
        "required": "لطفا نام خود را وارد کنید",
        "max_length": "تعداد حروف نام شما بالاتر از حد مجاز است"
    })
    email = forms.EmailField(max_length=200, label="ایمیل شما", widget=forms.EmailInput)
    title = forms.CharField(max_length=200, label="عنوان پیغام شما")
    message = forms.CharField(widget=forms.Textarea, label="پیغام شما")
