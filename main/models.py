from django.db import models
from ckeditor.fields import RichTextField


class Content(models.Model):
    name = models.CharField("Название", max_length=250)
    description = RichTextField("Содержание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ContentFile(models.Model):
    name = models.CharField("Название файла", max_length=250)
    category = models.ManyToManyField("Content")
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to='files/')
    date_month = models.PositiveIntegerField("Расчетный период: месяц", default=0)
    date_year = models.PositiveIntegerField("Расчетный период: год", default=2021)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
