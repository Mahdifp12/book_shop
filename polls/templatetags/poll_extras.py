from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter(name="d_jalali")
def jalali_date(value):
    return date2jalali(value)


@register.filter(name="t_jalali")
def jalali_time(value):
    time = datetime2jalali(value).strftime("%H:%M")
    return time
