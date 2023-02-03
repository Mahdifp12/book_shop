from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=300, verbose_name="ایمیل")
    title = models.CharField(max_length=300, verbose_name="عنوان")
    message = models.TextField(verbose_name="پیام تماس با ما")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    response = models.TextField(verbose_name="پاسخ توسط ادمین")
    is_read_by_admin = models.BooleanField(default=False, verbose_name="دیده شده توسط ادمین")

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "لیست تماس با ما"

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.FileField(upload_to="images")