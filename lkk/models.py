from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

#Список ГП и ЭСО
class Eso(models.Model):
    gp = models.CharField(max_length=100, verbose_name='Наименование ГП')

    def __str__(self):
        return self.gp
#Адреса
class Adres(models.Model):
    #
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adr_index = models.CharField(max_length=6, blank=False, verbose_name="Индекс")
    adr_region = models.CharField(max_length=100, blank=False, verbose_name="Субъект РФ")
    adr_rayon = models.CharField(max_length=100, blank=True, verbose_name="Район")
    adr_gorod = models.CharField(max_length=100, blank=True, verbose_name="Город")
    adr_naselpunkt = models.CharField(max_length=100, blank=True, verbose_name="Населенный пункт")
    adr_ulica = models.CharField(max_length=100, blank=True, verbose_name="Улица")
    adr_homenum = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    adr_kvar = models.CharField(max_length=10, blank=True, verbose_name="Квартира/Офис/Комната")
    adr_primechanie = models.TextField(max_length=500, blank=True, verbose_name='Примечание')

    def __str__(self):
        return self.adr_index+', район '+self.adr_rayon+', город '+self.adr_gorod+', нас.пункт '+self.adr_naselpunkt+', улица '+self.adr_ulica+', '+self.adr_homenum

    #Люди
class People(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fio_sname = models.CharField(max_length=80, verbose_name="Фамилия")
    fio_name = models.CharField(max_length=80, verbose_name="Имя")
    fio_lname = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    #ФИО в родительном падеже
    fio_sname_rod = models.CharField(max_length=80, verbose_name="Фамилия (в родительном падеже)")
    fio_name_rod = models.CharField(max_length=80, verbose_name="Имя (в родительном падеже)")
    fio_lname_rod = models.CharField(max_length=100, blank=True, verbose_name="Отчество (в родительном падеже)")
    #контактные данные
    cont_tel = PhoneNumberField(region='RU', blank=False, unique=True, verbose_name="Телефон")
    cont_tel_podtverzden = models.BooleanField(verbose_name='Телефонный номер подтвержден')
    cont_email = models.EmailField (blank=False, unique=True, verbose_name="Email")
    cont_email_podtverzden = models.BooleanField(verbose_name='E-mail подтвержден')
    doc_polnomochia = models.FileField(verbose_name='Сканированная копия документа, подтверждающее полномочия лица', blank=True)


    def __str__(self):
        return self.fio_sname+' '+self.fio_name+' '+self.fio_lname

class Doc_ur(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ucheriditelnie = models.FileField(verbose_name='Учредительные документы юридического лица')
    vipiska_egpul = models.FileField(verbose_name='Выписка из ЕГРЮЛ')

# Create your models here.
class Zayavitel_ur(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #данные о заявителе
    fio = models.ForeignKey(People, blank=False, null=True, related_name='zayavitel', on_delete=models.CASCADE, verbose_name="Заявитель")
    org_name = models.CharField(max_length=255, blank=True, verbose_name="Наименование организации")
    snils = models.CharField(max_length=11, blank=True, verbose_name="СНИЛС")
    inn = models.CharField(max_length=12, blank=True, verbose_name="ИНН")
    org_forma = models.CharField(max_length=255, blank=True, verbose_name="Организационно-правовая форма")
    org_ogrn = models.CharField(max_length=13, blank=True, verbose_name="ОГРН (ЮЛ)")
    org_data_egrul = models.DateField(verbose_name="Дата внесения записи в ЕГРЮЛ")
    #данные о руководителе
    ruk_fio = models.ForeignKey(People, blank=False, null=True, related_name='rukovod', on_delete=models.CASCADE, verbose_name='Руководитель')
    #данные о представителе
    pred_fio = models.ForeignKey(People, blank=False, null=True, related_name='predstavitel',on_delete=models.RESTRICT, verbose_name='Представитель')
    #pred_document = models.FileField(verbose_name="Документ подтверждающий полномочия представителя")
    pred_document_num = models.CharField(max_length=80, blank=True, verbose_name="Номер документа подтверждающего полномочия представителя")
    pred_document_date = models.DateField(verbose_name="Дата документа подтверждающего полномочия представителя")

    #Адрес юридический
    adr_ur = models.ForeignKey(Adres, blank=False, null=True, related_name='yuridicheskiy', on_delete=models.RESTRICT, verbose_name='Юридический адрес')
    #Адрес почтовый
    adr_post = models.ForeignKey(Adres, blank=False, null=True, related_name='pochtoviy', on_delete=models.RESTRICT, verbose_name='Почтовый адрес')
    adr_post_aya = models.CharField(max_length=100, blank=True, verbose_name="Абонентский ящик")
    adr_post_poluchatel = models.CharField(max_length=255, blank=True, verbose_name="Получатель")
    #Адрес фактический
    adr_fakt = models.ForeignKey(Adres, blank=False, null=True, related_name='fakticheskiy', on_delete=models.RESTRICT, verbose_name='Юридический адрес')

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
    tip_pris = models.CharField(choices=spisok_tipe_pris, max_length=2, blank=False, null=True, verbose_name='Тип присоединения')
    prichina_obr = models.CharField(choices=spisok_prichina_obr, max_length=2, blank=True, verbose_name='Причина обращения')
    vremenniy_tehpris = models.CharField(choices=[('ПВ', 'на период выполнения постоянной схемы электроснабжения'),
                                                  ('ПО', 'передвижных объектов')],
                                         blank=True, verbose_name='Временное присоединение', max_length=2)
    vremenniy_tehpris_srok = models.IntegerField(blank=True, null=True, verbose_name='сроком на (дней)')

    #Договор о технологическом подключении на постоянное электроснабжение
    name_so = models.CharField(default='ООО "Алтайская электросетевая компания"', blank=True, max_length=100, verbose_name='Наименование сетевой организации, с которой заключен договор')
    dog_tehpris_num = models.CharField(blank=True, max_length=30, verbose_name='№ договора')
    dog_tehpris_date = models.DateField(blank=True, null=True, verbose_name='Дата договора')
    dog_tehpris_file = models.FileField(blank=True, verbose_name='Сканированная копия договора')

    #Энергопринимающие устройства
    name_ustroystv = models.CharField(max_length=255, blank=False, null=True, verbose_name="Наименование устройств")
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
    type_mesnosti = models.CharField(choices=spisok_type_mesnosti, max_length=3, blank=False, null=True, verbose_name='Тип местности')
    kad_number = models.CharField(max_length=100, blank=True, verbose_name="Кадастровый номер")
    mestopolozenie_ustroystv = models.ForeignKey(Adres, blank=False, null=True, on_delete=models.CASCADE, verbose_name='Адрес присоединяемых энергопринимающих устройств')
    max_p = models.IntegerField(blank=False, null=True, verbose_name="Максимальная мощность устройств (всего), кВт")
    napr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=False, verbose_name='при напряжении')
    max_p_prisoed_ustr = models.IntegerField(blank=False, null=True, verbose_name="Максимальная мощность присоединяемых устройств, кВт")
    napr_prisoed_ustr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=False, verbose_name='при напряжении')
    max_p_rprisoed_ustr = models.IntegerField(blank=False, null=True, verbose_name="Максимальная мощность ранее присоединенных устройств, кВт")
    napr_rprisoed_ustr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=False, verbose_name='при напряжении')
    harakter_nagr = models.CharField(max_length=100, blank=False, null=True, verbose_name="Характер нагрузки")
    kat_nadeznosti =models.CharField(choices=spisok_kat_nadeznosti, default='3', blank=False, max_length=3, verbose_name='Категория надежности')
    vid_deyat_okved = models.CharField(max_length=100, blank=False, null=True, verbose_name="Вид деятельности по ОКВЭД 2")

    #Энергосбытовая организация
    spisok_vid_dogovora = [
        ('ЭС', 'Договор энергоснабжения'),
        ('ДКП', 'Договор купли-продажи'),
        ('ГОС', 'Госконтракт'),
        ('Пр.', 'Иной вид договора'),

    ]
    eso=models.ForeignKey(Eso, blank=True, null=True, on_delete=models.PROTECT)
    vid_dogovora = models.CharField(choices=spisok_vid_dogovora, max_length=3, blank=True  , verbose_name='Вид договора')
    dog_number = models.CharField(max_length=30, blank=True, verbose_name='Номер договора (если заключен)')
    dog_date = models.DateField(blank=True, null=True, verbose_name='Дата договора (если заключен)')
    persdannie_soglasie_eso = models.FileField(blank=True, verbose_name='Согласие на обработку персональных данных сетевой организацией и субъектом розничного рынка, с которым представитель заявителя намеревается заключить договор, обеспечивающий продажу электроэнергии на розничном рынке')

    #Документы и файлы
    ur_doc = models.ForeignKey(Doc_ur, null=True, on_delete=models.RESTRICT, verbose_name='Документы юр.лица')
    plan_raspolozenia = models.FileField(null=True, verbose_name='План расположения энергопринимающих устройств')
    pravo_sobstvennosti = models.FileField(null=True, verbose_name='Документ, подтверждающий право собственности на объект или иное предусмотренное законом основание')
    mkd = models.BooleanField(default=False, verbose_name='Осуществляется присоединение устройств, находящихся в нежилых помещениях многоквартирного дома')
    mkd_vru = models.CharField(choices=[('Да', 'Да'), ('Нет','Нет')], blank=True, null=True, max_length=3, verbose_name='Проектом на многоквартирный дом для нежилого помещения предусмотрено индивидуальное вводно-распределительное устройство')
    mkd_soglasie = models.FileField(blank=True, verbose_name='Документ, подтверждающий согласие на присоединение устройств в нежилом помещении в многоквартирном доме')
    snt =  models.BooleanField(default=False, verbose_name='Осуществляется присоединение устройств на территории садоводческого, огороднического или дачного некоммерческого объединения граждан с использованием объектов инфраструктуры и другого имущества общего пользования этого объединения')
    snt_spravka = models.FileField(blank=True, verbose_name='Справка о количестве земельных участков, расположенных в границах территории садоводства или огородничества')
    snt_soglasie = models.FileField(blank=True, verbose_name='Согласие всех граждан, осуществляющих ведение садоводства или огородничества на земельных участках на территории садоводства или огородничества, на обработку персональных данных сетевой организацией и субъектом розничного рынка')
    gsk = models.BooleanField(default=False, verbose_name='Осуществляется присоединение устройств, принадлежащих потребительскому кооперативу (гаражно-строительному, гаражному кооперативу) либо его членам')
    gsk_spravka = models.FileField(blank=True, verbose_name='Справка о количестве гаражей либо иных объектов, расположенных в границах территории кооператива')
    sobstvennikov_neskolko = models.BooleanField(default=False, verbose_name='Осуществляется присоединение устройств на объекте/земельном участке, правоустанавливающие документы которого подразумевают долевую/совместную собственность')
    soglasie_sobstvennikov = models.FileField(blank=True, verbose_name='Согласие всех сособственников (их уполномоченных представителей) на присоединение к сетям сетевой организации')
    protivoavariynaya_avtomatic = models.BooleanField(default=False, verbose_name='Энергопринимающие устройства будут присоединены к устройствам противоаварийной автоматики')
    protivoavariynaya_avtomatica = models.FileField(blank=True, verbose_name='Перечень и мощность энергопринимающих устройств, присоединяемых к устройствам противоаварийной автоматики')
    doc_tehpris = models.FileField(blank=True, verbose_name='Документ, подтверждающий ранее присоединенную мощность')


    #Способ обмена документами
    sposob_obena_doc = models.CharField(choices=[('ПР','Выдать представителю'), ('ПО','Направить почтой'), ('ЭВ','Электронное взаимодействие')],
                                        default='ЭВ', max_length=2, verbose_name='Способ обмена документами')
    gotovnost_doc = models.CharField(choices=[('sms', 'sms-уведомлением'), ('ema', 'по email'), ('tel', 'по телефону')],
                                     max_length=3, verbose_name='О готовности документов сообщить', default='ema')
    persdannie = models.BooleanField(blank=False, null=True, verbose_name='В соответствии с Федеральным законом от 27 июля 2006 года № 152-ФЗ "О персональных данных" даю свое согласие на обработку своих персональных данных по настоящей заявке ООО "Алтайская электросетевая компания", сетевой организацией и субъектом розничного рынка, с которым имеется намерение заключить договор, обеспечивающий продажу электроэнергии на розничном рынке')
    persdannie_file = models.FileField(blank=True, verbose_name='Согласие на обработку персональных данных ООО «Алтайская электросетевая компания», сетевой организации и субъектом розничного рынка, с которым имеется намерение заключить договор, обеспечивающий продажу электроэнергии на розничном рынке')


    created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    # def clean(self):
    #     #тип присоединения
    #     if self.tip_pris == 'PP' and self.prichina_obr is None:
    #         raise ValidationError(('Причина обращения не выбрана'))
        # if self.tip_pris == 'VR' and self.vremenniy_tehpris_srok is None :
        #     raise ValidationError('')
        # if self.vremenniy_tehpris_srok > 366:
        #     raise ValidationError('Присоединение передвижных объектов может осуществляется сроком до 12 месяцев (365/366 дней)')

    def publish(self):
        self.published_date = timezone.now()
        self.save()




class Test(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
