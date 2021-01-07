from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Zayavitel_ur(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #данные о заявителе
    fio_sname = models.CharField(max_length=80, verbose_name="Фамилия")
    fio_name = models.CharField(max_length=80, verbose_name="Имя")
    fio_lname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    org_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наименование организации")
    snils = models.CharField(max_length=11, blank=True, null=True, verbose_name="СНИЛС")
    inn = models.CharField(max_length=12, blank=True, null=True, verbose_name="ИНН")
    org_forma = models.CharField(max_length=255, blank=True, null=True, verbose_name="Организационно-правовая форма")
    org_ogrn = models.CharField(max_length=13, blank=True, null=True, verbose_name="ОГРН (ЮЛ)")
    org_data_egrul = models.DateField(verbose_name="Дата внесения записи в ЕГРЮЛ")
    #данные о руководителе
    ruk_sname = models.CharField(max_length=80, verbose_name="Фамилия")
    ruk_name = models.CharField(max_length=80, verbose_name="Имя")
    ruk_lname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    #данные о представителе
    pred_sname = models.CharField(max_length=80, blank=True, null=True, verbose_name="Фамилия")
    pred_name = models.CharField(max_length=80, blank=True, null=True, verbose_name="Имя")
    pred_lname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    pred_document = models.FileField(verbose_name="Документ подтверждающий полномочия представителя")
    pred_document_num = models.CharField(max_length=80, blank=True, null=True, verbose_name="Номер документа")
    pred_document_date = models.DateField()

    #контактные данные
    cont_tel = PhoneNumberField(region='RU', null=False, blank=False, unique=True, verbose_name="Телефон")
    cont_email = models.EmailField(null=False, blank=False, unique=True, verbose_name="Email")

    #Адрес юридический
    adr_ul_index = models.CharField(max_length=6, blank=False, null=False, verbose_name="Индекс")
    adr_ul_region = models.CharField(max_length=100, blank=False, null=False, verbose_name="Субъект РФ")
    adr_ul_rayon = models.CharField(max_length=100, blank=True, null=True, verbose_name="Район")
    adr_ul_gorod = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    adr_ul_naselpunkt = models.CharField(max_length=100, blank=True, null=True, verbose_name="Населенный пункт")
    adr_ul_ulica = models.CharField(max_length=100, blank=True, null=True, verbose_name="Улица")
    adr_ul_homenum = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер дома")
    adr_ul_kvar = models.CharField(max_length=10, blank=True, null=True, verbose_name="Квартира/Офис/Комната")

    #Адрес почтовый
    adr_post_index = models.CharField(max_length=6, blank=False, null=False, verbose_name="Индекс")
    adr_post_region = models.CharField(max_length=100, blank=False, null=False, verbose_name="Субъект РФ")
    adr_post_rayon = models.CharField(max_length=100, blank=True, null=True, verbose_name="Район")
    adr_post_gorod = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    adr_post_naselpunkt = models.CharField(max_length=100, blank=True, null=True, verbose_name="Населенный пункт")
    adr_post_ulica = models.CharField(max_length=100, blank=True, null=True, verbose_name="Улица")
    adr_post_homenum = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер дома")
    adr_post_kvar = models.CharField(max_length=10, blank=True, null=True, verbose_name="Квартира/Офис/Комната")
    adr_post_aya = models.CharField(max_length=100, blank=True, null=True, verbose_name="Абонентский ящик")
    adr_post_poluchatel = models.CharField(max_length=255, blank=True, null=True, verbose_name="Получатель")

    #Адрес факт
    adr_fakt_index = models.CharField(max_length=6, blank=False, null=False, verbose_name="Индекс")
    adr_fakt_region = models.CharField(max_length=100, blank=False, null=False, verbose_name="Субъект РФ")
    adr_fakt_rayon = models.CharField(max_length=100, blank=True, null=True, verbose_name="Район")
    adr_fakt_gorod = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    adr_fakt_naselpunkt = models.CharField(max_length=100, blank=True, null=True, verbose_name="Населенный пункт")
    adr_fakt_ulica = models.CharField(max_length=100, blank=True, null=True, verbose_name="Улица")
    adr_fakt_homenum = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер дома")
    adr_fakt_kvar = models.CharField(max_length=10, blank=True, null=True, verbose_name="Квартира/Офис/Комната")

    #платежные реквизиты
    plat_kpp = models.CharField(max_length=9, blank=False, null=False, verbose_name="КПП")
    plat_bik = models.CharField(max_length=9, blank=False, null=False, verbose_name="БИК")
    plat_bank = models.CharField(max_length=255, blank=False, null=False, verbose_name="Наименование банка")
    plat_rs = models.CharField(max_length=21, blank=False, null=False, verbose_name="Расчетный счет")
    plat_ks = models.CharField(max_length=21, blank=False, null=False, verbose_name="Корреспондентский счет")

    # created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title