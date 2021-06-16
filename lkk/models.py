from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

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
    '''база данных физических лиц'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    people_type = models.CharField(max_length=3, blank=False, null=True, choices=[('fiz','Физическое лицо'),
                                            ('ruk','Руководитель организации'),
                                            ('pre','Представитель организации'),], verbose_name='Тип')
    fio_sname = models.CharField(max_length=80, verbose_name="Фамилия")
    fio_name = models.CharField(max_length=80, verbose_name="Имя")
    fio_lname = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    #snils = models.CharField(max_length=11, blank=True, null=True, verbose_name="СНИЛС")
    dolznost = models.CharField(max_length=255, blank=True, null=True, verbose_name="Должность")
    #ФИО в родительном падеже
    fio_sname_rod = models.CharField(max_length=80, verbose_name="Фамилия (в родительном падеже)")
    fio_name_rod = models.CharField(max_length=80, verbose_name="Имя (в родительном падеже)")
    fio_lname_rod = models.CharField(max_length=100, blank=True, verbose_name="Отчество (в родительном падеже)")
    #Документ, удостоверяющий личность
    snils = models.CharField(max_length=11, blank=True, verbose_name="СНИЛС")
    doc_vid = models.CharField(max_length=80, blank=True, null=True, verbose_name='Вид документа', default='Паспорт')
    doc_seria = models.CharField(max_length=80, blank=True, null=True, verbose_name='Серия')
    doc_number = models.CharField(max_length=80, blank=True, null=True, verbose_name='Номер')
    doc_vidan = models.CharField(max_length=80, blank=True, null=True, verbose_name='Выдан')
    doc_data = models.DateField(blank=True, null=True, verbose_name='Дата выдачи')
    doc_file = models.FileField(blank=True, null=True, verbose_name='Сканированная копия документа')
    #контактные данные
    cont_tel = PhoneNumberField(region='RU', blank=False, unique=True, verbose_name="Телефон")
    cont_tel_podtverzden = models.BooleanField(blank=True, null=True, verbose_name='Телефонный номер подтвержден')
    cont_email = models.EmailField (blank=False, unique=True, verbose_name="Email")
    cont_email_podtverzden = models.BooleanField(blank=True, null=True, verbose_name='E-mail подтвержден')
    #Адрес юридический
    adr_main = models.ForeignKey(Adres, blank=True, null=True, related_name='mestonahozdenie_fiz', on_delete=models.RESTRICT, verbose_name='Адрес места регистрации')
    #Адрес почтовый
    adr_post = models.ForeignKey(Adres, blank=True, null=True, related_name='pochtoviy_fiz', on_delete=models.RESTRICT, verbose_name='Почтовый адрес')
    adr_post_aya = models.CharField(max_length=100, blank=True, verbose_name="Абонентский ящик")
    adr_post_poluchatel = models.CharField(max_length=255, blank=True, verbose_name="Получатель")
    #Адрес фактический
    adr_fakt = models.ForeignKey(Adres, blank=True, null=True, related_name='fakticheskiy_fiz', on_delete=models.RESTRICT, verbose_name='Адрес места жительства')
    #Документ подтверждающий полномочия
    doc_polnomochia = models.FileField(verbose_name='Сканированная копия документа, подтверждающее полномочия лица', blank=True)



    def clean(self):
        #if self.fio is None:
        #    raise ValidationError({'fio' : _('Выбирите заявителя')})
        if self.people_type == 'fiz':
            if self.doc_vid is None:
                raise ValidationError({'doc_vid' : _('Введите тип документа подтверждающего личность')})
            if self.doc_number is None:
                raise ValidationError({'doc_number' : _('Введите номер документа подтверждающего личность')})
            if self.doc_seria is None:
                raise ValidationError({'doc_seria' : _('Введите серию документа подтверждающего личность')})
            if not self.doc_file :
                raise ValidationError({'doc_file' : _('Прикрепите скан-копию документа подтверждающего личность')})
            if self.doc_vidan is None:
                raise ValidationError({'doc_vidan' : _('Введите кем выдан документ подтверждающий личность')})
            if self.doc_data is None:
                raise ValidationError({'doc_data' : _('Введите дату выдачи документа подтверждающего личность')})
            if self.adr_main is None:
                raise ValidationError({'adr_main' : _('Для физического лица обязательно необходимо указать адрес регистрации')})
            if self.adr_post is None:
                raise ValidationError({'adr_post' : _('Для физического лица обязательно необходимо указать адрес для отправки корреспонденции')})
            if self.adr_fakt is None:
                raise ValidationError({'adr_fakt' : _('Для физического лица обязательно необходимо указать адрес местонахождения')})
        else:
            if self.dolznost is None:
                raise ValidationError({'dolznost' : _('Введите должность')})

    def __str__(self):
        return self.fio_sname + ' ' + self.fio_name + ' ' + self.fio_lname

# Create your models here.
class Zayavitel_ur(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #данные о заявителе
    #fio = models.ForeignKey(People, blank=False, null=True, related_name='zayavitel', on_delete=models.CASCADE, verbose_name="Заявитель")
    org_name = models.CharField(max_length=255, blank=False, null=True, verbose_name="Наименование организации")
    #snils = models.CharField(max_length=11, blank=True, verbose_name="СНИЛС")
    inn = models.CharField(max_length=12, blank=False, null=True, verbose_name="ИНН")
    org_forma = models.CharField(max_length=255, blank=False, null=True, verbose_name="Организационно-правовая форма")
    org_ogrn = models.CharField(max_length=13, blank=False, null=True, verbose_name="ОГРН (ЮЛ)")
    org_data_egrul = models.DateField(verbose_name="Дата внесения записи в ЕГРЮЛ")
    #данные о руководителе
    ruk_fio = models.ForeignKey(People, blank=False, null=True, related_name='rukovod', on_delete=models.CASCADE, verbose_name='Руководитель')
    #данные о представителе
    pred_fio = models.ForeignKey(People, blank=True, null=True, related_name='predstavitel',on_delete=models.RESTRICT, verbose_name='Представитель',
                                 help_text='Выберите этот пункт, если интересы организации будет представлять лицо, отличное от руководителя')
    #pred_document = models.FileField(verbose_name="Документ подтверждающий полномочия представителя")
    pred_document_num = models.CharField(max_length=80, blank=True, null=True, verbose_name="Номер документа подтверждающего полномочия представителя")
    pred_document_date = models.DateField(blank=True, null=True, verbose_name="Дата документа подтверждающего полномочия представителя")

    #Адрес юридический
    adr_ur = models.ForeignKey(Adres, blank=False, null=True, related_name='yuridicheskiy', on_delete=models.RESTRICT, verbose_name='Юридический адрес')
    #Адрес почтовый
    adr_post = models.ForeignKey(Adres, blank=False, null=True, related_name='pochtoviy', on_delete=models.RESTRICT, verbose_name='Почтовый адрес')
    adr_post_aya = models.CharField(max_length=100, blank=True, verbose_name="Абонентский ящик")
    adr_post_poluchatel = models.CharField(max_length=255, blank=True, verbose_name="Получатель")
    #Адрес фактический
    adr_fakt = models.ForeignKey(Adres, blank=False, null=True, related_name='fakticheskiy', on_delete=models.RESTRICT, verbose_name='Фактический адрес')

    #платежные реквизиты
    plat_kpp = models.CharField(max_length=9, blank=False, verbose_name="КПП")
    plat_bik = models.CharField(max_length=9, blank=False, verbose_name="БИК")
    plat_bank = models.CharField(max_length=255, blank=False, verbose_name="Наименование банка")
    plat_rs = models.CharField(max_length=21, blank=False, verbose_name="Расчетный счет")
    plat_ks = models.CharField(max_length=21, blank=False, verbose_name="Корреспондентский счет")

    created_date = models.DateTimeField(default=timezone.now)

    def clean(self):
        #if self.fio is None:
        #    raise ValidationError({'fio' : _('Выбирите заявителя')})
        if self.org_name is None:
            raise ValidationError({'org_name' : _('Заполните данные об организации')})
        if self.pred_fio is not None and self.pred_document_num is None:
            raise ValidationError({'pred_document_num' : _('Необходимо ввести номер документа, подтверждающего полномочия представителя')})
        if self.pred_fio is not None and self.pred_document_date is None:
            raise ValidationError({'pred_document_date' : _('Необходимо ввести дату документа, подтверждающего полномочия представителя')})
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.org_name

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
    fio = models.ForeignKey(People, blank=False, null=True, related_name='zayavitel', on_delete=models.CASCADE,
                            verbose_name="Заявитель", help_text='Выберите кто будет выступать заявителем.')
    org = models.ForeignKey(Zayavitel_ur, blank=True, null=True, related_name='organizaciya', on_delete=models.CASCADE, verbose_name='Организация заявитель',
                            help_text='Выберите организацию являющуюся заявителем, если заявка подаётся от имени юридического лица.'
                                      ' Если заявка подаётся от имени физического лица оставьте это поле не заполненным.')
    tip_pris = models.CharField(choices=spisok_tipe_pris, max_length=2, blank=False, null=True, verbose_name='Тип присоединения')
    prichina_obr = models.CharField(choices=spisok_prichina_obr, max_length=2, blank=True, null=True, verbose_name='Причина обращения')
    vremenniy_tehpris = models.CharField(choices=[('ПВ', 'на период выполнения постоянной схемы электроснабжения'),
                                                  ('ПО', 'передвижных объектов')],
                                         blank=True, verbose_name='Временное присоединение', max_length=2,
                                         help_text='Под передвижными объектами понимаются энергопринимающие устройства,'
                                                   ' предназначенные для эксплуатации с периодическим перемещением и установкой на различных территориях')
    vremenniy_tehpris_srok = models.IntegerField(blank=True, null=True, verbose_name='сроком на (дней)',
                                                 help_text='Присоединение передвижных объектов может осуществляется сроком до 12 месяцев (365/366 дней)')

    #Договор о технологическом подключении на постоянное электроснабжение
    name_so = models.CharField(default='ООО "Алтайская электросетевая компания"', blank=True, max_length=100,
                               verbose_name='Наименование сетевой организации, с которой заключен договор')
    dog_tehpris_num = models.CharField(blank=True, max_length=30, verbose_name='№ договора')
    dog_tehpris_date = models.DateField(blank=True, null=True, verbose_name='Дата договора')
    dog_tehpris_file = models.FileField(blank=True, verbose_name='Сканированная копия договора',
                                        help_text='Максимальный размер файла - 5 Мб.'
                                                  ' Допустимые форматы документа - doc, docx, xls, xlsx, odt, ods, pdf, tif, tiff, jpg, bmp, png, gif, txt, rtf, rar, zip.'
                                                  ' Если требуется приложить более одного файла к одному документу, поместите их в архив.')

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
    type_mesnosti = models.CharField(choices=spisok_type_mesnosti, max_length=3, blank=False, null=True, verbose_name='Тип местности',
                                     help_text='Города и поселки городского типа относятся к городской местности. Остальные типы населенных пунктов - к сельской.')
    kad_number = models.CharField(max_length=100, blank=True, verbose_name="Кадастровый номер",
                                  help_text='Укажите кадастровый номер земельного участка (помещения, здания),'
                                            ' на котором располагаются (будут располагаться) энергопринимающие устройства'
                                            ' для наиболее точного определения местоположения объекта.'
                                            ' Данная информация указана в правоустанавливающих документах на земельный участок (помещение, здание).')
    mestopolozenie_ustroystv = models.ForeignKey(Adres, blank=False, null=True, on_delete=models.CASCADE,
                                                 verbose_name='Адрес присоединяемых энергопринимающих устройств')
    max_p = models.IntegerField(blank=False, null=True, verbose_name="Максимальная мощность устройств (всего), кВт",
                                help_text='Указывается максимальная мощность энергопринимающих устройств всего:'
                                          ' присоединяемых по данной заявке и ранее присоединенных (если были присоединены ранее)')
    napr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=False, verbose_name='при напряжении',
                            help_text='Уровень напряжения в сети переменного тока в точке присоединения')
    max_p_prisoed_ustr = models.IntegerField(blank=False, null=True, verbose_name="Максимальная мощность присоединяемых устройств, кВт",
                                             help_text='Указывается максимальная мощность устройств, присоединяемых по данной заявке')
    napr_prisoed_ustr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=False, verbose_name='при напряжении',
                                         help_text='Уровень напряжения в сети переменного тока в точке присоединения')
    max_p_rprisoed_ustr = models.IntegerField(blank=True, null=True, verbose_name="Максимальная мощность ранее присоединенных устройств, кВт",
                                              help_text='Указывается в случае, если объект уже присоединен к сетям,'
                                                        ' в соответствии с документами, подтверждающими технологическое присоединение')
    napr_rprisoed_ustr = models.CharField(choices=spisok_napr, null=True, max_length=4, blank=True, verbose_name='при напряжении',
                                          help_text='Уровень напряжения в сети переменного тока в точке присоединения')
    harakter_nagr = models.CharField(choices=[('Бытовая','Бытовая'),
                                              ('Производственная','Производственная'),
                                              ('Смешанная','Смешанная')], max_length=100, blank=False, null=True, verbose_name="Характер нагрузки")
    kat_nadeznosti =models.CharField(choices=spisok_kat_nadeznosti, default='3', blank=False, max_length=3, verbose_name='Категория надежности')
    kolvo_tochek = models.IntegerField(default=1, blank=False, null=True, verbose_name='Количество точек присоединения')
    vid_deyat_okved = models.CharField(max_length=100, blank=False, null=True, verbose_name="Вид деятельности по ОКВЭД 2",
                                       help_text='Укажите вид экономической деятельности. Если ни один из вариантов не подходит, выберите значение "Прочее".')
    etapi = models.TextField(blank=False, null=True, verbose_name='Сроки проектирования и поэтапного введения в эксплуатацию объекта'
                                                                  ' (в том числе по этапам и очередям), планируемое поэтапное'
                                                                  ' распределение максимальной мощности')
    #Энергосбытовая организация
    spisok_vid_dogovora = [
        ('ЭС', 'Договор энергоснабжения'),
        ('ДКП', 'Договор купли-продажи'),
        ('ГОС', 'Госконтракт'),
        ('Пр.', 'Иной вид договора'),

    ]
    eso=models.ForeignKey(Eso, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Наименование ГП (ЭСО)',
                          help_text='Укажите организацию (гарантирующего поставщика),'
                                    ' с которой планируется заключить договор,'
                                    ' обеспечивающий продажу электрической энергии (мощности).')
    vid_dogovora = models.CharField(choices=spisok_vid_dogovora, max_length=3, blank=True  , verbose_name='Вид договора',
                                    help_text='Укажите вид договора, обеспечивающий продажу электроэнергии (мощности) на розничном рынке,'
                                              ' который планируете заключить с энергосбытовой организацией:'
                                              ' договор энергоснабжения или договор купли-продажи электроэнергии.'
                                              ' При заключении договора купли-продажи электроэнергии требуется заключение договора '
                                              'на оказание услуг по передаче электроэнергии с сетевой организацией.')
    dog_number = models.CharField(max_length=30, blank=True, verbose_name='Номер договора (если заключен)',
                                  help_text='Укажите реквизиты договора, обеспечивающего продажу электрической энергии, если договор уже заключен')
    dog_date = models.DateField(blank=True, null=True, verbose_name='Дата договора (если заключен)',
                                help_text='Укажите реквизиты договора, обеспечивающего продажу электрической энергии, если договор уже заключен')
    persdannie_soglasie_eso = models.FileField(blank=True, verbose_name='Согласие на обработку персональных данных сетевой организацией и субъектом розничного рынка, с которым представитель заявителя намеревается заключить договор, обеспечивающий продажу электроэнергии на розничном рынке')

    #Документы и файлы
    ucheriditelnie = models.FileField(blank=True, null=True, verbose_name='Учредительные документы юридического лица')
    vipiska_egpul = models.FileField(blank=True, null=True, verbose_name='Выписка из ЕГРЮЛ')
    #ur_doc = models.ForeignKey(Doc_ur, null=True, on_delete=models.RESTRICT, verbose_name='Документы юр.лица')
    plan_raspolozenia = models.FileField(null=True, verbose_name='План расположения энергопринимающих устройств')
    pravo_sobstvennosti = models.FileField(null=True, verbose_name='Документ, подтверждающий право собственности на объект или иное предусмотренное законом основание')
    mkd = models.BooleanField(default=False,
                              verbose_name='Осуществляется присоединение устройств, находящихся в нежилых помещениях многоквартирного дома',
                              help_text='Поставьте отметку в случае присоединения энергопринимающих устройств,'
                                        ' находящихся в нежилых помещениях, расположенных в многоквартирных домах'
                                        ' и иных объектах капитального строительства')
    mkd_vru = models.CharField(choices=[('Да', 'Да'), ('Нет','Нет')], blank=True, null=True, max_length=3,
                               verbose_name='Проектом на многоквартирный дом для нежилого помещения'
                                            ' предусмотрено индивидуальное вводно-распределительное устройство',
                               help_text='- Укажите <Да> в случае, если проектом на многоквартирный дом для соответствующего'
                                         ' нежилого помещения предусмотрено индивидуальное вводно-распределительное устройство'
                                         ' с непосредственным присоединением к питающей линии сетевой организации.'
                                         '- Укажите <Нет> в обратном случае.')
    mkd_soglasie = models.FileField(blank=True, verbose_name='Документ, подтверждающий согласие на присоединение устройств'
                                                             ' в нежилом помещении в многоквартирном доме',
                                    help_text='Под согласием понимается согласие на организацию присоединения нежилого помещения'
                                              ' отдельными линиями от вводного устройства (вводно-распределительного устройства,'
                                              ' главного распределительного щита),'
                                              ' установленного на вводе питающей линии сетевой организации'
                                              ' в соответствующем здании или его обособленной части.'
                                              'Таким документом является: В случае наличия организации, осуществляющей управление'
                                              ' многоквартирным домом, наделенной соответствующими полномочиями:'
                                              '- Документ, подтверждающий согласие организации, осуществляющей управление '
                                              'многоквартирным домом, В случае отсутствия такой организации или отсутствия у'
                                              ' нее полномочий: - Документ, подтверждающий согласие общего собрания владельцев'
                                              ' жилых помещений многоквартирного дома.')
    snt =  models.BooleanField(default=False,
                               verbose_name='Осуществляется присоединение устройств на территории садоводческого,'
                                            ' огороднического или дачного некоммерческого объединения граждан'
                                            ' с использованием объектов инфраструктуры и'
                                            ' другого имущества общего пользования этого объединения',
                               help_text='Поставьте отметку в случае, если: - Вы ведете садоводство, огородничество или'
                                         ' дачное хозяйство в индивидуальном порядке на территории садоводческого,'
                                         ' огороднического или дачного некоммерческого объединения и '
                                         '- присоединение энергопринимающих устройств осуществляется с использованием объектов'
                                         ' инфраструктуры и другого имущества общего пользования этого объединения.')
    snt_spravka = models.FileField(blank=True, verbose_name='Справка о количестве земельных участков, расположенных в границах территории садоводства или огородничества')
    snt_soglasie = models.FileField(blank=True, verbose_name='Согласие всех граждан, осуществляющих ведение садоводства'
                                                             ' или огородничества на земельных участках на территории садоводства или огородничества,'
                                                             ' на обработку персональных данных сетевой организацией и субъектом розничного рынка',
                                    help_text='Заполненное всеми гражданами, осуществляющими ведение садоводства или огородничества на земельных участках,'
                                              ' расположенных в границах территории садоводства или огородничества, иными правообладателями объектов недвижимости,'
                                              ' расположенных в границах территории садоводства или огородничества, или собственниками,'
                                              ' или иными законными владельцами гаражей либо иных объектов, расположенных в границах территории кооператива,'
                                              ' в отношении энергопринимающих устройств которых подается заявка, согласие на обработку персональных данных '
                                              'сетевой организацией и субъектом розничного рынка, с которым заявитель намеревается заключить договор, обеспечивающий'
                                              ' продажу электрической энергии (мощности) на розничном рынке')
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


    status = models.CharField(choices=[('save','Сохранено, но не направлено'),
                                       ('nonf', 'Заявка заполнена, но не сформирована'),
                                       ('send', 'Направлена, ожидает рассмотрения'),
                                       ('edit','Возвращена на доработку'),
                                       ('vrab','Принята в работу')],
                                        default='save', max_length=4, verbose_name='Статус заявки', blank=True, null=True)
    status_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    status_error = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    zaya_file = models.FileField(blank=True, verbose_name='Заявка')
    #published_date = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.fio.people_type != 'fiz':
            if not self.ucheriditelnie:
                raise ValidationError({'ucheriditelnie': _('Заявителем является юридическое лицо, приложите документ')})
            if not self.vipiska_egpul:
                raise ValidationError({'vipiska_egpul': _('Заявителем является юридическое лицо, приложите документ')})
        if self.fio.people_type == 'fiz' and not self.org is None:
            raise ValidationError({'org': _('Заявителем является физическое лицо, наименование организации в этом случае не заполнятеся')})
        if self.tip_pris == 'PP' and self.prichina_obr is None:
            raise ValidationError({'prichina_obr' : _('Причина обращения не выбрана')})
        if self.tip_pris == 'VR' and self.vremenniy_tehpris is None:
            raise ValidationError({'vremenniy_tehpris': _(
                'Не выбраны параметры временного присоединения.'
                ' Под передвижными объектами понимаются энергопринимающие устройства, предназначенные для эксплуатации с периодическим перемещением и установкой на различных территориях')})
        if self.tip_pris == 'VR' and self.vremenniy_tehpris == 'ПО':
            if self.vremenniy_tehpris_srok is None:
                raise ValidationError({'vremenniy_tehpris_srok': _('Присоединение передвижных объектов может осуществляется сроком до 12 месяцев (365/366 дней), срок не может быть пустым')})
            elif self.vremenniy_tehpris_srok > 366 or self.vremenniy_tehpris_srok < 1:
                raise ValidationError({'vremenniy_tehpris_srok': _('Присоединение передвижных объектов может осуществляется сроком до 12 месяцев (365/366 дней). Вы указали невозможный срок.')})
        if self.tip_pris == 'VR' and self.vremenniy_tehpris == 'ПВ' and (self.name_so is None or self.dog_tehpris_date is None or self.dog_tehpris_num is None or self.dog_tehpris_file is None):
            raise ValidationError({'name_so': _('Нужно заполнить все сведения про договор о технологическом подключении на постоянное электроснабжение')})
        if self.mkd and self.mkd_vru is None:
            raise ValidationError({'mkd_vru': _('- Укажите <Да> в случае, если проектом на многоквартирный дом для соответствующего нежилого помещения предусмотрено индивидуальное вводно-распределительное устройство с непосредственным присоединением к питающей линии сетевой организации.'
                                                '- Укажите <Нет> в обратном случае.')})
        if self.mkd and self.mkd_vru == 'Нет' and not self.mkd_soglasie:
            raise ValidationError({'mkd_soglasie' : _('Приложите файл! Под согласием понимается согласие на организацию присоединения нежилого помещения отдельными линиями от вводного устройства (вводно-распределительного устройства, главного распределительного щита), установленного на вводе питающей линии сетевой организации в соответствующем здании или его обособленной части.')})
        if self.snt and not self.snt_soglasie:
            raise ValidationError({'snt_soglasie': _('Приложите согласие')})
        if self.snt and not self.snt_spravka:
            raise ValidationError({'snt_spravka': _('Приложите справку')})
        if self.gsk and not self.gsk_spravka:
            raise ValidationError({'gsk_spravka': _('Приложите справку')})
        if self.sobstvennikov_neskolko and not self.soglasie_sobstvennikov:
            raise ValidationError({'soglasie_sobstvennikov': _('Приложите согласие')})
        if self.protivoavariynaya_avtomatic and not self.protivoavariynaya_avtomatica:
            raise ValidationError({'protivoavariynaya_avtomatica': _('Приложите перечень')})
        if not self.persdannie:
            raise ValidationError({'persdannie': _('Мы не сможем принять заявку без согласия на обработку персональных данных')})

        # if self.vremenniy_tehpris_srok > 366:
        #     raise ValidationError('Присоединение передвижных объектов может осуществляется сроком до 12 месяцев (365/366 дней)')

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Documenty(models.Model):
    '''Документы по заявкам о тех.присоединении'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='autor')
    #тут косяк нужно исправит поле zayavitel
    zayavitel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='zayavitel_doc')
    doc_type = models.CharField(choices=[('ДоТП', 'Договор техприсоединения'),
                                         ('ТУ', 'Технические условия'),
                                         ('АТП', 'Акт технологического присоединения'),
                                         ('Счет', 'Счет'),
                                         ('Пись', 'Письмо'),
                                         ('Проч', 'Прочие документы'),
                                         ], max_length=4, verbose_name='Тип документа')
    comment = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(blank=True, verbose_name='Файл')

class Obracheniya(models.Model):
    '''Обращения потребителя'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fio = models.ForeignKey(People, blank=False, null=True, related_name='zayavitel_obr', on_delete=models.CASCADE,
                            verbose_name="Обращение от имени", help_text='Выберите лицо от имени которого направляется обращение.')
    org = models.ForeignKey(Zayavitel_ur, blank=True, null=True, related_name='organizaciya_obr', on_delete=models.CASCADE, verbose_name='Обращение от имени организации',
                            help_text='Выберите организацию от имени которой направляется обращение.')
    obrachenie_type = models.CharField(choices=[('БЗП>', 'Сообщить о хищении, неучтенном потреблении электроэнергии'),
                                         ('Спр', 'Запрос справочной информации и консультации'),
                                         ('Жал', 'Жалоба'),
                                         ], max_length=4, verbose_name='Тип обращения')
    comment = models.TextField(null=True, blank=False, verbose_name='Текст обращения')
    file = models.FileField(blank=True, verbose_name='Приложить материалы')
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=[('save','Сохранено, но не направлено'),
                                       ('nonf', 'Заявка заполнена, но не сформирована'),
                                       ('send', 'Направлена, ожидает рассмотрения'),
                                       ('edit','Возвращена на доработку'),
                                       ('vrab','Принята в работу')],
                                        default='save', max_length=4, verbose_name='Статус заявки', blank=True, null=True)
    def clean(self):
        if self.fio.peole_type == 'fiz' and not self.org is None:
            raise ValidationError(
                {'org': _('Заявителем является физическое лицо, наименование организации в этом случае не заполнятеся')})

class Epu(models.Model):
    '''Энергопринимающие устройства'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #zayavitel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='zayavitel_epu')
    epu_ps = models.CharField(null=True, blank=True, max_length=100, verbose_name='Наименование высоковольной ПС')
    epu_yacheyka = models.CharField(null=True, blank=True, max_length=30, verbose_name='Номер высоковольной ячейки')
    epu_linia = models.CharField(null=True, blank=True, max_length=30, verbose_name='Наименование отходящей высоковольной линии')
    epu_opora_vv = models.CharField(null=True, blank=True, max_length=10, verbose_name='Номер опоры высоковольной линии')
    epu_ktp = models.CharField(null=True, blank=True, max_length=10, verbose_name='Наименование КТП/ТП')
    epu_fider = models.CharField(null=True, blank=True, max_length=30, verbose_name='Наименование фидера 0,4 кВ')
    epu_opora_nv = models.CharField(null=True, blank=True, max_length=10, verbose_name='Номер опоры 0,4 кВ')
    epu_grbp = models.CharField(null=True, blank=True, max_length=255, verbose_name='Описание границы раздела балансовой принадлежности')
    epu_p_max = models.IntegerField(null=True, blank=True, verbose_name='Максимальная мощность')
    epu_adres = models.ForeignKey(Adres, blank=False, null=True, on_delete=models.CASCADE,
                                  verbose_name='Адрес присоединяемых энергопринимающих устройств')
    comment = models.TextField(null=True, blank=False, verbose_name='Комментарий')
    file = models.FileField(blank=True, null=True, verbose_name='Приложить материалы')
    created_date = models.DateTimeField(default=timezone.now)

class Zayavka_pu(models.Model):
    '''Заявки касаемо ПУ'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fio = models.ForeignKey(People, blank=False, null=True, related_name='zayavitel_pu', on_delete=models.CASCADE,
                            verbose_name="Заявитель", help_text='Выберите лицо от имени которого направляется заявка.')
    org = models.ForeignKey(Zayavitel_ur, blank=True, null=True, related_name='organizaciya_pu', on_delete=models.CASCADE, verbose_name='Организация заявитель',
                            help_text='Выберите организацию от имени которой направляется заявка.')
    obrachenie_type = models.CharField(choices=[('522-ФЗ>', 'Установка/замена/допуск в эксплуатацию прибора учета электрической энергии'),
                                         ('Допуск', 'Допуск в эксплуатацию прибора учета электрической энергии'),
                                         ('Снятие', 'Снятие показаний существующего прибора учета электрической энергии'),
                                         ('Устан', 'Оборудование точки поставки приборами учета электрической энергии'),
                                         ('Показ', 'Передать показания прибора учета электрической энергии'),
                                         ], max_length=7, verbose_name='Тип обращения')
    epu = models.ForeignKey(Epu, on_delete=models.CASCADE, related_name='epu', verbose_name='Энергопринимающее устройство')
    pu_type = models.CharField(null=True, blank=True, max_length=100, verbose_name='Тип прибора учета')
    pu_number = models.CharField(null=True, blank=True, max_length=100, verbose_name='Номер прибора учета')
    pu_mesto_ustanovki = models.CharField(null=True, blank=True, max_length=100, verbose_name='Место установки прибора учета')
    pu_pokazanie = models.IntegerField(null=True, blank=True, verbose_name='Показание прибора учета в настоящий момент')
    comment = models.TextField(null=True, blank=False, verbose_name='Дополнительная информация')
    file = models.FileField(blank=True, null=True, verbose_name='Приложить материалы')
    created_date = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.obrachenie_type == 'Показ':
            if not self.pu_number:
                raise ValidationError({'pu_number': _('При передаче показаний необходимо обязательно передать номер ПУ')})
            if not self.pu_type:
                raise ValidationError({'pu_type': _('При передаче показаний необходимо обязательно передать тип ПУ')})
        if self.obrachenie_type == 'Допуск':
            if not self.pu_number:
                raise ValidationError({'pu_number': _('Для допуска ПУ необходимо обязательно указать его номер')})
            if not self.pu_type:
                raise ValidationError({'pu_type': _('Для допуска ПУ необходимо обязательно указать его тип')})
            if not self.pu_mesto_ustanovki:
                raise ValidationError({'pu_mesto_ustanovki': _('Для допуска ПУ необходимо обязательно указать его место установки')})


class Test(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
