from django.db import models


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

