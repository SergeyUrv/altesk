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
    fio_lname = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    org_name = models.CharField(max_length=255, blank=True, verbose_name="Наименование организации")
    snils = models.CharField(max_length=11, blank=True, verbose_name="СНИЛС")
    inn = models.CharField(max_length=12, blank=True, verbose_name="ИНН")
    org_forma = models.CharField(max_length=255, blank=True, verbose_name="Организационно-правовая форма")
    org_ogrn = models.CharField(max_length=13, blank=True, verbose_name="ОГРН (ЮЛ)")
    org_data_egrul = models.DateField(verbose_name="Дата внесения записи в ЕГРЮЛ")
    #данные о руководителе
    ruk_sname = models.CharField(max_length=80, verbose_name="Фамилия")
    ruk_name = models.CharField(max_length=80, verbose_name="Имя")
    ruk_lname = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    #данные о представителе
    pred_sname = models.CharField(max_length=80, blank=True, verbose_name="Фамилия")
    pred_name = models.CharField(max_length=80, blank=True, verbose_name="Имя")
    pred_lname = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    pred_document = models.FileField(verbose_name="Документ подтверждающий полномочия представителя")
    pred_document_num = models.CharField(max_length=80, blank=True, verbose_name="Номер документа")
    pred_document_date = models.DateField(verbose_name="Дата документа")

    #контактные данные
    cont_tel = PhoneNumberField(region='RU', blank=False, unique=True, verbose_name="Телефон")
    cont_email = models.EmailField blank=False, unique=True, verbose_name="Email")

    #Адрес юридический
    adr_ul_index = models.CharField(max_length=6, blank=False, verbose_name="Индекс")
    adr_ul_region = models.CharField(max_length=100, blank=False, verbose_name="Субъект РФ")
    adr_ul_rayon = models.CharField(max_length=100, blank=True, verbose_name="Район")
    adr_ul_gorod = models.CharField(max_length=100, blank=True, verbose_name="Город")
    adr_ul_naselpunkt = models.CharField(max_length=100, blank=True, verbose_name="Населенный пункт")
    adr_ul_ulica = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    adr_ul_homenum = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    adr_ul_kvar = models.CharField(max_length=10, blank=True, verbose_name="Квартира/Офис/Комната")

    #Адрес почтовый
    adr_post_index = models.CharField(max_length=6, blank=False, verbose_name="Индекс")
    adr_post_region = models.CharField(max_length=100, blank=False, verbose_name="Субъект РФ")
    adr_post_rayon = models.CharField(max_length=100, blank=True, verbose_name="Район")
    adr_post_gorod = models.CharField(max_length=100, blank=True, verbose_name="Город")
    adr_post_naselpunkt = models.CharField(max_length=100, blank=True, verbose_name="Населенный пункт")
    adr_post_ulica = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    adr_post_homenum = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    adr_post_kvar = models.CharField(max_length=10, blank=True, verbose_name="Квартира/Офис/Комната")
    adr_post_aya = models.CharField(max_length=100, blank=True, verbose_name="Абонентский ящик")
    adr_post_poluchatel = models.CharField(max_length=255, blank=True, verbose_name="Получатель")

    #Адрес факт
    adr_fakt_index = models.CharField(max_length=6, blank=False, verbose_name="Индекс")
    adr_fakt_region = models.CharField(max_length=100, blank=False, verbose_name="Субъект РФ")
    adr_fakt_rayon = models.CharField(max_length=100, blank=True, verbose_name="Район")
    adr_fakt_gorod = models.CharField(max_length=100, blank=True, verbose_name="Город")
    adr_fakt_naselpunkt = models.CharField(max_length=100, blank=True, verbose_name="Населенный пункт")
    adr_fakt_ulica = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    adr_fakt_homenum = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    adr_fakt_kvar = models.CharField(max_length=10, blank=True, verbose_name="Квартира/Офис/Комната")

    #платежные реквизиты
    plat_kpp = models.CharField(max_length=9, blank=False, verbose_name="КПП")
    plat_bik = models.CharField(max_length=9, blank=False, verbose_name="БИК")
    plat_bank = models.CharField(max_length=255, blank=False, verbose_name="Наименование банка")
    plat_rs = models.CharField(max_length=21, blank=False, verbose_name="Расчетный счет")
    plat_ks = models.CharField(max_length=21, blank=False, verbose_name="Корреспондентский счет")

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Zayavka(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spisok_tipe_pris = [
        ('VR' , 'Временное присоединение'),
        ('PP' , 'Постоянное присоединение')
    ]
    spisok_prichina_obr = [
        ('IS', 'Изменение схемы без пересмотра мощности'),
        ('NP', 'Новое присоединение'),
        ('UM', 'Увеличение максимальной мощности')
    ]
    tip_pris = models.CharField(choices=spisok_tipe_pris, max_length=2, blank=False, verbose_name='Тип присоединения')
    prichina_obr = models.CharField(choices=spisok_prichina_obr, max_length=2, verbose_name='Причина обращения')
    #Энергопринимающие устройства
    name_ustroystv = models.CharField(max_length=255, blank=False, verbose_name="Наименование устройств")
    spisok_type_mesnosti = [
        ('gor', 'Городская'),
        ('sel', 'Сельская'),
    ]
    spisok_napr =[
        ('0,22', '0,22 кВ'),
        ('0,4', '0,4 кВ'),
        ('6', '6 кВ'),
        ('10', '10 кВ'),
        ('35', '35 кВ'),
        ('110', '110 кВ'),
        ('220', '220 кВ'),
    ]
    spisok_kat_nadeznosti =[
        ('3', 'III'),
        ('2', 'II'),
        ('1', 'I'),
        ('12', 'I и II'),
        ('13', 'I и III'),
        ('23', 'II и III'),
        ('123', 'I, II и III'),
    ]
    type_mesnosti = models.CharField(choices=spisok_tipe_pris, max_length=2, blank=False, verbose_name='Тип местности')
    kad_number = models.CharField(max_length=100, blank=True, verbose_name="Кадастровый номер")
    mestopolozenie_ustroystv = models.TextField(max_length=500, verbose_name='Адрес присоединяемых энергопринимающих устройств')
    max_p = models.IntegerField(blank=False, verbose_name="Максимальная мощность устройств (всего), кВт")
    napr = models.CharField(choices=spisok_napr, max_length=4, blank=False, verbose_name='при напряжении')
    max_p_prisoed_ustr = models.IntegerField(blank=False, verbose_name="Максимальная мощность присоединяемых устройств, кВт")
    napr_prisoed_ustr = models.CharField(choices=spisok_napr, max_length=4, blank=False, verbose_name='при напряжении')
    max_p_rprisoed_ustr = models.IntegerField(blank=False, verbose_name="Максимальная мощность ранее присоединенных устройств, кВт")
    napr_rprisoed_ustr = models.CharField(choices=spisok_napr, max_length=4, blank=False, verbose_name='при напряжении')
    harakter_nagr = models.CharField(max_length=100, blank=False, verbose_name="Характер нагрузки")
    kat_nadeznosti =models.CharField(choices=spisok_tipe_pris, blank=False, max_length=3, blank=False, verbose_name='Категория надежности')
    vid_deyat_okved = models.CharField(max_length=100, blank=False, verbose_name="Вид деятельности по ОКВЭД 2")

    created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.tip_pris == 'PP' and self.prichina_obr is None:
            raise ValidationError('Причина обращения не выбрана')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Spravochnik(models.Model):
    gp = models.CharField(max_length=100, verbose_name='Наименование ГП')

    def __str__(self):
        return self.title

class Eso(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
