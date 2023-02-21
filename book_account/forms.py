from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput()
    )
