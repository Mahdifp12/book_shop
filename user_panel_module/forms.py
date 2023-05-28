from django import forms

from book_account.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام شما"}),
            'last_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "ایمیل شما"}),
            'avatar': forms.FileInput(attrs={
                "class": "form-control",
                "placeholder": "عنوان پیفام شما",
            }),
            'address': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "پیغام شما",
                "rows": "3",
                "cols": "20",
                "id": "message"})
        }

        labels = {
            'first_name': "نام",
            'last_name': "نام خانوادگی",
            'avatar': "تصویر پروفایل",
            'address': "آدرس",

        }
        error_messages = {
            'first_name': {
                'required': 'لطفا نام خود را وارد کنید',
                'max_length': 'تعداد حروف نام شما بیشتر از حد مجاز است'
            },
            'last_name': {
                'required': 'لطفا نام خانوادگی خود را وارد کنید',
            },
            'address': {
                'required': 'لطفا آدرس خود را وارد کنید',
            }
        }