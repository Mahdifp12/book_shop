from django.db import models
from jalali_date import datetime2jalali, date2jalali

from book_account.models import User


# Create your models here.


class ArticleCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=250, unique=True, verbose_name="عنوان دسته بندی url")
    parent = models.ForeignKey('ArticleCategory',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               verbose_name="دسته بندی والد")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیر فعال")

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی های مقاله"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=400, unique=True, allow_unicode=True, verbose_name="عنوان مقاله در URL")
    image = models.ImageField(upload_to="images/articles/", verbose_name="تصویر مقاله")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    text = models.TextField(verbose_name="متن مقاله")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیر فعال")
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="دسته بندی ها")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده", null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def get_jalali_time(self):
        return datetime2jalali(self.create_date).strftime("%H:%M")

    def get_jalali_date(self):
        return date2jalali(self.create_date)

    def __str__(self):
        return self.title
