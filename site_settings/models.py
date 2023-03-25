from django.db import models


# Create your models here.

class SiteSettings(models.Model):
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")
    site_name = models.CharField(max_length=250, verbose_name="نام سایت")
    address = models.CharField(max_length=250, verbose_name="آدرس")
    phone = models.CharField(max_length=250, null=True, verbose_name="شماره تلفن")
    fax = models.CharField(max_length=250, null=True, verbose_name="فکس")
    email = models.CharField(max_length=250, null=True, verbose_name="ایمیل")
    copy_right_text = models.TextField(verbose_name="متن کپی رایت")
    site_logo = models.ImageField(upload_to="images/site_settings/", verbose_name="لوگو سایت")
    site_url = models.CharField(max_length=250, verbose_name="دامنه سایت")
    about_us = models.TextField(verbose_name="درباره ما")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name
