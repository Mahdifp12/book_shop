from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/users_avatar", verbose_name="تصویر آواتار", null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی ایمیل")
    about_user = models.TextField(verbose_name="درباره کاربر", null=True, blank=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()

        return self.email
