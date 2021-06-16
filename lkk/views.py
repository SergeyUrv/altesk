from django.shortcuts import render, get_object_or_404

from main.models import ContentPotr
from .forms import ZayavkaForm, Zayavitel_yur, Zayavitel_people, Adres_form, Zayavitel_form, Epu_form, Obracheniya_form
from .models import People, Adres, Zayavitel_ur, Zayavka, Epu, Obracheniya
from django.shortcuts import redirect
from django.utils import timezone
from docxtpl import DocxTemplate

# импорты для рендеринга заявки
from django.conf import settings
import os
import uuid

from django.contrib import messages

# импорт логин-декоратора
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


# функция вывода редактирования формы
# запрос, ID в базе, Модель, Форма модели, перенаправить после сохранения формы, заголовок, какой рендерить шаблон
def get_form(request, pkk, SModel, Model_form, redir, title, rendering='lkk/profile_form_edit.html'):
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    try:
        find_object = SModel.objects.get(pk=pkk, author=request.user)
        object_nayden = True
    except SModel.DoesNotExist:
        object_nayden = False
    # people1 = get_object_or_404(People, author=request.user)
    if request.method == "POST":
        if object_nayden:
            form = Model_form(request.POST, request.FILES, instance=find_object, users=request.user)
        else:
            form = Model_form(request.POST, request.FILES, users=request.user)
        if form.is_valid():
            vform = form.save(commit=False)
            # people.doc_polnomochia = People(request.FILES['doc_polnomochia'])
            vform.author = request.user
            vform.created_date = timezone.now()
            vform.status = 'nonf'
            vform.status_date = timezone.now()
            vform.save()
            return redirect(redir)
    else:
        if object_nayden:
            form = Model_form(instance=find_object, users=request.user)
        else:
            form = Model_form(users=request.user)
    return render(request, rendering, {'form': form, 'title': title, "content": content})


# добавление и редактирование заявки
@login_required()
def zayavka_new(request, pkk):
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit' or item.status == 'nonf':
            # item._zaya_file = zayavka_tp_render(item)
            return get_form(request=request, pkk=pkk, SModel=Zayavka, Model_form=ZayavkaForm, redir='zayavki',
                            title='Подача заявки на тех.присоединение',
                            rendering='lkk/zayavka_new.html')
        else:
            return redirect('zayavki')
    except Zayavka.DoesNotExist:
        return get_form(request=request, pkk=pkk, SModel=Zayavka, Model_form=ZayavkaForm, redir='zayavki',
                        title='Подача заявки на тех.присоединение', rendering='lkk/zayavka_new.html')


# добавление и редактирование людей
@login_required()
def profile_edit(request, pkk):
    return get_form(request=request, pkk=pkk, SModel=People, Model_form=Zayavitel_people, redir='person',
                    title='Данные о персонах',
                    rendering='lkk/people_form_edit.html')


# добавление и редактирование адресов
@login_required()
def profile_adres_edit(request, pkk):
    return get_form(request=request, pkk=pkk, SModel=Adres, Model_form=Adres_form, redir='adres',
                    title='Данные об адресах')


# добавление и редактирование юр.лица
@login_required()
def zayavitel_edit(request, pkk):
    return get_form(request, pkk, Zayavitel_ur, Zayavitel_form, 'zayavitel', 'Данные о заявителе')


# добавление и редактирование энергопринимающего устройства
@login_required()
def epu_edit(request, pkk):
    return get_form(request, pkk, Epu, Epu_form, 'epu', 'Данные об энергопринимающем устройстве')

# добавление и редактирование обращения
@login_required()
def obracheniya_edit(request, pkk):
    try:
        item = Obracheniya.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit' or item.status == 'nonf':
            return get_form(request=request, pkk=pkk, SModel=Obracheniya, Model_form=Obracheniya_form, redir='obracheniya',
                            title='Подача обращения',
                            rendering='lkk/obracheniya_edit.html')
        else:
            return redirect('obracheniya')
    except Obracheniya.DoesNotExist:
        return get_form(request=request, pkk=pkk, SModel=Obracheniya, Model_form=Obracheniya_form, redir='obracheniya',
                        title='Подача обращения', rendering='lkk/obracheniya_edit.html')

# удаление epu
@login_required()
def epu_del(request, pkk):
    try:
        epu1 = Epu.objects.get(pk=pkk, author=request.user)
        epu1.delete()
    except Epu.DoesNotExist:
        epu_nayden = False
    return redirect('epu')


# удаление людей
@login_required()
def profile_del(request, pkk):
    try:
        people1 = People.objects.get(pk=pkk, author=request.user)
        people1.delete()
    except People.DoesNotExist:
        people_nayden = False
    return redirect('person')


# удаление адресов
@login_required()
def profile_adres_del(request, pkk):
    try:
        people1 = Adres.objects.get(pk=pkk, author=request.user)
        people1.delete()
    except Adres.DoesNotExist:
        people_nayden = False
    return redirect('adres')


# удаление юр.лица
@login_required()
def zayavitel_del(request, pkk):
    try:
        item = Zayavitel_ur.objects.get(pk=pkk, author=request.user)
        item.delete()
    except Zayavitel_ur.DoesNotExist:
        people_nayden = False
    return redirect('zayavitel')


@login_required()
def zayavka_del(request, pkk):
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit':
            item.delete()
        else:
            return redirect('zayavki')
    except Zayavka.DoesNotExist:
        people_nayden = False
    return redirect('zayavki')

# удаление обращения
@login_required()
def obracheniya_del(request):
    pass

# отправка заявки
@login_required()
def zayavka_send(request, pkk):
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit':
            item.status_date = timezone.now()
            item.created_date = timezone.now()
            item.status = 'send'
            item.save()
    except Zayavka.DoesNotExist:
        people_nayden = False
    return redirect('zayavki')


# просмотр списка людей
@login_required()
def epu_view(request):
    epu = Epu.objects.filter(author=request.user)
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_epu_view.html', {'epu': epu, 'title': 'Энергопринимающие устройства', "content": content})


# просмотр списка людей
@login_required()
def profile_view(request):
    fio = People.objects.filter(author=request.user)
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_view.html', {'fio': fio, 'title': 'Персоны', "content": content})


# просмотр списка адресов
@login_required()
def profile_adres(request):
    adres = Adres.objects.filter(author=request.user)
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_adres_view.html', {'adres': adres, 'title': 'Адреса', "content": content})


# просмотр списка юр.лиц
@login_required()
def zayavitel(request):
    zaya = Zayavitel_ur.objects.filter(author=request.user)
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_zayavitel_view.html',
                  {'zaya': zaya, 'title': 'Заявители', 'user': request.user, "content": content})


# просмотр списка заявок
@login_required()
def zayavka_view(request):
    zaya = Zayavka.objects.filter(author=request.user)
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_zayavka_view.html',
                  {'zaya': zaya, 'title': 'Заявки на технологическое присоединение',
                   'user': request.user, "content": content})

# просмотр списка обращений
@login_required()
def obracheniya_view(request):
    pass


# Вывод главной страницы ЛКК
@login_required
def main_lk(request):
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/main.html', {"content": content})


# создание файла с заявкой
def zayavka_tp_render(item):
    '''рендеринг вердовского шаблона заявки значениями полей заявки
    '''
    # locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    # открываем шаблон заявки
    doc = DocxTemplate(os.path.join(settings.STATIC_ROOT, 'Заявка на ТП.docx'))
    # обрабатываем поля касающиеся типа присоединения
    if item.tip_pris == 'PP':
        tip_pris = item.get_tip_pris_display() + ', причина обращения: ' + item.get_prichina_obr_display()
    else:
        if item.vremenniy_tehpris == 'ПО':
            tip_pris = item.get_tip_pris_display() + ' ' + item.get_vremenniy_tehpris_display() + ', сроком на ' + str(
                item.vremenniy_tehpris_srok)
        else:
            tip_pris = item.get_tip_pris_display() + ' ' + item.get_vremenniy_tehpris_display() + ' по договору тех.присоединения с ' + \
                       item.name_so + ' №' + item.dog_tehpris_num + ' от ' + item.dog_tehpris_date.strftime("%d.%m.%Y")
    # обрабатываем кадастровый номер если есть
    if item.kad_number is not None:
        kad_number = 'Кадастровый номер' + item.kad_number
    else:
        kad_number = ''
    # обрабатываем наименование ГП если есть
    if item.eso is not None:
        eso = item.eso.gp
    else:
        eso = ''
    # обрабатываем реквизиты договора если есть
    if item.dog_number is None or item.dog_date is None:
        dogovor = ''
    else:
        dogovor = ' №' + item.dog_number + ' от ' + item.dog_date.strftime("%d.%m.%Y")
    # собираем ФИО в строку
    fio = item.fio.fio_sname + ' ' + item.fio.fio_name + ' ' + item.fio.fio_lname

    def check_filedfile(filedfile):
        '''Проверяем есть ли файл, ставить ли галочку'''
        if filedfile:
            return 'V'
        else:
            return '-'

    # обрабатываем поля в зависимости от типа заявителя физ.лицо или юр.лицо
    if item.org:
        zayavitel_name = item.org.org_name
        inn = '(ИНН:' + item.org.inn + ')'
        org_ogrn = item.org.org_ogrn
        org_data_egrul = item.org.org_data_egrul.strftime("%d.%m.%Y")
        adr_ur = item.org.adr_ur
        adr_fakt = item.org.adr_fakt
        adr_post = item.org.adr_post
        doc_vid = ''
        doc_seria = ''
        doc_number = ''
        doc_vidan = ''
        doc_data = ''
        doc_file = ''
    else:
        zayavitel_name = fio
        inn = ''
        org_ogrn = ''
        org_data_egrul = ''
        adr_ur = item.fio.adr_main
        adr_fakt = item.fio.adr_fakt
        adr_post = item.fio.adr_post
        doc_vid = item.fio.doc_vid
        doc_seria = item.fio.doc_seria
        doc_number = item.fio.doc_number
        doc_vidan = item.fio.doc_vidan
        doc_data = item.fio.doc_data.strftime("%d.%m.%Y")
        doc_file = check_filedfile(item.fio.doc_file)
    # создаем массив переменных для рендеринга шаблона
    context = {'org_name': zayavitel_name,
               'inn': inn,
               'org_ogrn': org_ogrn,
               'org_data_egrul': org_data_egrul,
               'adr_ur': adr_ur,
               'adr_fakt': adr_fakt,
               'adr_post': adr_post,  # +', ая.'+item.org.adr_post_aya+', получатель: '+item.org.adr_post_poluchatel,
               'doc_vid': doc_vid,
               'doc_seria': doc_seria,
               'doc_number': doc_number,
               'doc_vidan': doc_vidan,
               'doc_data': doc_data,
               'doc_file': doc_file,
               'name_ustroystv': item.name_ustroystv,
               'tip_pris': tip_pris,
               'mestopolozenie_ustroystv': item.mestopolozenie_ustroystv,
               'max_p': item.max_p,
               'napr': item.napr,
               'max_p_prisoed_ustr': item.max_p_prisoed_ustr,
               'napr_prisoed_ustr': item.napr_prisoed_ustr,
               'max_p_rprisoed_ustr': item.max_p_rprisoed_ustr,
               'napr_rprisoed_ustr': item.napr_rprisoed_ustr,
               'harakter_nagr': item.harakter_nagr,
               'kat_nadeznosti': item.get_kat_nadeznosti_display(),
               'vid_deyat_okved': item.vid_deyat_okved,
               'kad_number': kad_number,
               'eso': eso,
               'vid_dogovora': item.get_vid_dogovora_display(),
               'dogovor': dogovor,
               'kolvo_tochek': item.kolvo_tochek,
               'fio': fio,
               'dolznost': item.fio.dolznost,
               'tel': item.fio.cont_tel,
               'date': item.created_date.strftime("%d.%m.%Y"),
               'persdannie_soglasie_eso': check_filedfile(item.persdannie_soglasie_eso),
               'ucheriditelnie': check_filedfile(item.ucheriditelnie),
               'vipiska_egpul': check_filedfile(item.vipiska_egpul),
               'plan_raspolozenia': check_filedfile(item.plan_raspolozenia),
               'pravo_sobstvennosti': check_filedfile(item.pravo_sobstvennosti),
               'mkd_soglasie': check_filedfile(item.mkd_soglasie),
               'snt_spravka': check_filedfile(item.snt_spravka),
               'snt_soglasie': check_filedfile(item.snt_soglasie),
               'gsk_spravka': check_filedfile(item.gsk_spravka),
               'soglasie_sobstvennikov': check_filedfile(item.soglasie_sobstvennikov),
               'protivoavariynaya_avtomatica': check_filedfile(item.protivoavariynaya_avtomatica),
               'persdannie_file': check_filedfile(item.persdannie_file),
               'doc_tehpris': check_filedfile(item.doc_tehpris),
               'etapi': item.etapi,
               }
    # рендерим шаблон
    doc.render(context)
    if not item.zaya_file:
        path = 'zayavki_tp/Заявка на ТП %s-%s.docx' % (item.pk, str(uuid.uuid4()))
    else:
        path = item.zaya_file.name
    # сохраняем сформированную заявку
    doc.save(os.path.join(settings.MEDIA_ROOT, path))
    return (path)


@login_required()
def zayavka_create(request, pkk):
    '''нелюходимо доделать'''
    '''вьюшка вызывает создание заявки в вердовском формате'''
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'nonf':
            item.zaya_file = zayavka_tp_render(item)
            item.status_date = timezone.now()
            item.created_date = timezone.now()
            item.status = 'save'
            item.save()
    except Zayavka.DoesNotExist:
        people_nayden = False
    return redirect('zayavki')


@login_required()
def zayavka_detail(request, pkk):
    '''детализированный просмотр заявки'''
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit':
            return render(request, 'lkk/profile_zayavka_detail.html',
                          {'zaya': item,
                           'user': request.user})
    except Zayavka.DoesNotExist:
        people_nayden = False
    return redirect('zayavki')

#####################Вьюшки для админки персонала

# просмотр списка заявок персоналом
@staff_member_required
def zayavka_view_admin(request):
    zaya = Zayavka.objects.all
    content = ContentPotr.objects.get(name="Личный кабинет потребителя")
    return render(request, 'lkk/profile_zayavka_view_admin.html',
                  {'zaya': zaya, 'title': 'Заявки на технологическое присоединение',
                   'user': request.user, "content": content})

# принять заявку в работу
@staff_member_required()
def zayavka_status_vrab(request, pkk):
    try:
        item = Zayavka.objects.get(pk=pkk)
        if item.status == 'send':
            item.status_date = timezone.now()
            item.status = 'vrab'
            item.save()
    except Zayavka.DoesNotExist:
        pass
    return redirect('zayavki_admin')

# вернуть на доработку
@staff_member_required()
def zayavka_status_edit(request, pkk):
    pass

# приложить договор
@staff_member_required()
def zayavka_status_obr(request, pkk):
    pass

# аннулировать заявку
@staff_member_required()
def zayavka_status_canc(request, pkk):
    pass

# отметить что договор подписан
@staff_member_required()
def zayavka_status_doc(request, pkk):
    pass

# выполнено тех.присоединение со стороны СО
@staff_member_required()
def zayavka_status_wpod(request, pkk):
    pass

# выполнен тех.прис. - приложить документы
@staff_member_required()
def zayavka_status_done(request, pkk):
    pass




