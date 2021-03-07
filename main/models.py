from django.db import models
from ckeditor.fields import RichTextField

class ContentMain(models.Model):
    name = models.CharField("Название", max_length=250)
    section = models.CharField("Раздел", max_length=250, default="", blank=True)
    description = RichTextField("Содержание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья в разделе 'Основные'"
        verbose_name_plural = "Статьи в разделе 'Основные'"

class ContentPotr(models.Model):
    name = models.CharField("Название", max_length=250)
    section = models.CharField("Раздел", max_length=250, default="Потребителям", blank=True)
    description = RichTextField("Содержание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья в разделе 'Потребителям'"
        verbose_name_plural = "Статьи в разделе 'Потребителям'"

class ContentRaskrInf(models.Model):
    name = models.CharField("Название", max_length=250)
    section = models.CharField("Раздел", max_length=250, default="Раскрытие информации", blank=True)
    description = RichTextField("Содержание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья в разделе 'Раскрытие информации'"
        verbose_name_plural = "Статьи в разделе 'Раскрытие информации'"

class ContentFile(models.Model):
    name = models.CharField("Название файла", max_length=250)
    content_potr = models.ManyToManyField("ContentPotr", verbose_name="Раздел 'Потребителям'", blank=True)
    content_raskrinf = models.ManyToManyField("ContentRaskrInf", verbose_name="Раздел 'Раскрытие информации'", blank=True)
    content_main = models.ManyToManyField("ContentMain", verbose_name="Раздел 'Основные'", blank=True)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to='files/')
    date_month = models.PositiveIntegerField("Расчетный период: месяц", default=0)
    date_quarter = models.PositiveIntegerField("Расчетный период: квартал", default=0)
    date_year = models.PositiveIntegerField("Расчетный период: год", default=2021)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
