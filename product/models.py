from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
from book_account.models import User


# Create your models here.

class BookCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')

    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')

    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")

    parent = models.ForeignKey('BookCategory', null=True, on_delete=models.CASCADE, verbose_name="دسته بندی والد",
                               blank=True)

    def __str__(self):
        return f'({self.title}) - ({self.url_title})'

    class Meta:
        verbose_name = "دسته بندی کتاب"
        verbose_name_plural = "دسته بندی کتاب ها"


class BookAuthor(models.Model):
    author_name = models.CharField(max_length=300, db_index=True, verbose_name="نام نویسنده")
    url_name = models.CharField(max_length=300, db_index=True, verbose_name="اسم در URL")
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")
    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return self.author_name


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")

    image = models.ImageField(upload_to="images/books", verbose_name="عکس کتاب", null=True, blank=True)

    category = models.ManyToManyField(
        BookCategory,
        related_name="book_categories",
        verbose_name="دسته بندی های کتاب",
    )

    author = models.ForeignKey(BookAuthor, null=True, on_delete=models.CASCADE, verbose_name="نویسنده")

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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب")
    quantity = models.PositiveIntegerField(default=1, verbose_name="مقدار محصول")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"

    def __str__(self):
        return f"{self.user} - {self.book}"
