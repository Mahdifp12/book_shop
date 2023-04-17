from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name="d_jalali")
def jalali_date(value):
    return date2jalali(value)
