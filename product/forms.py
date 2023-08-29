from django import forms


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(
        label="تعداد",
        min_value=1,
        widget=forms.NumberInput()
    )
