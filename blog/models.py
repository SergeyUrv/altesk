from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from mptt.models import MPTTModel, TreeForeignKey
import mptt

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Меню")
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name="URL-адрес")
    category_title = models.TextField(verbose_name="Описание разделов меню", blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Родитель")

    class MPTTMeta:
        order_insertion_by = ['name']
mptt.register(Genre, order_insertion_by=['name'])

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_category = TreeForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, related_name='Cat', verbose_name='Выберите пункт меню')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    url_name = models.CharField(max_length=200)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title