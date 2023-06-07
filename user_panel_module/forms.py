from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from book_account.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'address',
            'about_user',
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
                "placeholder": "تصویر پروفایل شما",
                "rows": "3",
                "cols": "20",
                "id": "message"}),

            'about_user': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "درباره شما",
                "rows": "6",
                "cols": "20", })
        }

        labels = {
            'first_name': "نام",
            'last_name': "نام خانوادگی",
            'avatar': "تصویر پروفایل",
            'address': "آدرس",
            'about_user': "درباره شما",

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


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label="رمز عبور فعلی",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور فعلی"
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ],
    )
    password = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور جدید"
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ],
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور جدید",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "تکرار رمز عبور جدید"
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ],
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('رمز عبور و تکرار رمز عبور مغایرت ندارد')
