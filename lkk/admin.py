from django.contrib import admin
from .models import Zayavitel_ur, Zayavka, Eso, Adres, People, Doc_ur
# Register your models here.

admin.site.register(Zayavitel_ur)
admin.site.register(Zayavka)
admin.site.register(Eso)
admin.site.register(Adres)
admin.site.register(People)
admin.site.register(Doc_ur)