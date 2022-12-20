from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.

class BookCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')

    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')

    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")

    def __str__(self):
        return f'({self.title}) - ({self.url_title})'

    class Meta:
        verbose_name = "دسته بندی کتاب"
        verbose_name_plural = "دسته بندی کتاب ها"


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")

    category = models.ManyToManyField(
        BookCategory,
        related_name="book_categories",
        verbose_name="دسته بندی های کتاب",

    )

    price = models.IntegerField(null=True, verbose_name="قیمت")

    short_description = models.CharField(max_length=400, null=True, db_index=True, verbose_name="توضیحات کوتاه")

    description = models.TextField(verbose_name="توضیحات اصلی", db_index=True)

    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")

    slug = models.SlugField(default="", null=False, allow_unicode=True, db_index=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'({self.title}) - ({self.price})'

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"


class BookTag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='عنوان تگ', db_index=True)

    book = models.ForeignKey(Book, max_length=200, on_delete=models.CASCADE, related_name="book_tags")

    class Meta:
        verbose_name = 'تگ کتاب'
        verbose_name_plural = "تگ های کتاب ها"

    def __str__(self):
        return self.caption
