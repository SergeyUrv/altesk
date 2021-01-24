from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ZayavkaForm, Zayavitel_yur, Zayavitel_people, Adres_form, Zayavitel_form
from .models import People, Adres, Zayavitel_ur, Zayavka
from django.shortcuts import redirect
from django.utils import timezone



# Create your views here.

#вывод формы входа
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile_ur(request):
    if request.method == "POST":
        form1 = Zayavitel_yur(request.POST)
        form2 = Zayavitel_people(request.POST)
        if form1.is_valid() and form2.is_valid():
            zayavitel1 = form1.save(commit=False)
            zayavitel2 = form2.save(commit=False)
            zayavitel1.author = request.user
            zayavitel1.created_date = timezone.now()
            zayavitel1.fio = zayavitel2.pk
            zayavitel1.save()
            return redirect('zayavka_detail', pk=zayavitel1.pk)
    else:
        form1 = Zayavitel_yur()
        form2 = Zayavitel_people()
    return render(request, 'lkk/profile.html', {'form1': form1, 'form2': form2, 'title': 'Редактирование'})

#@login_required
#def profile(request, step):

# функция вывода редактирования формы
# запрос, ID в базе, Модель, Форма модели, перенаправить после сохранения формы, заголовок, какой рендерить шаблон
def get_form(request, pkk, SModel, Model_form, redir, title, rendering='lkk/profile_form_edit.html'):
    try:
        find_object = SModel.objects.get(pk=pkk, author=request.user)
        object_nayden = True
    except SModel.DoesNotExist:
        object_nayden = False
    #people1 = get_object_or_404(People, author=request.user)
    if request.method == "POST":
        if object_nayden:
            form = Model_form(request.POST, request.FILES, instance=find_object, users=request.user)
        else:
            form = Model_form(request.POST, request.FILES, users=request.user)
        if form.is_valid():
            vform = form.save(commit=False)
            #people.doc_polnomochia = People(request.FILES['doc_polnomochia'])
            vform.author = request.user
            vform.created_date = timezone.now()
            vform.status = 'save'
            vform.status_date = timezone.now()
            vform.save()
            return redirect(redir)
    else:
        if object_nayden:
            form = Model_form(instance=find_object, users=request.user)
        else:
            form = Model_form(users=request.user)
    return render(request, rendering, {'form': form, 'title': title})

# добавление и редактирование заявки
def zayavka_new(request, pkk):
    try:
        item = Zayavka.objects.get(pk=pkk, author=request.user)
        if item.status == 'save' or item.status == 'edit':
            return get_form(request=request, pkk=pkk, SModel=Zayavka, Model_form=ZayavkaForm, redir='zayavki',
                            title='Подача заявки на тех.присоединение',
                            rendering='lkk/zayavka_new.html')
        else:
            return redirect('zayavki')
    except Zayavka.DoesNotExist:
        return get_form(request=request, pkk=pkk, SModel=Zayavka, Model_form=ZayavkaForm, redir='zayavki',
                        title='Подача заявки на тех.присоединение', rendering='lkk/zayavka_new.html')


# добавление и редактирование людей
def profile_edit(request, pkk):
    return get_form(request=request, pkk=pkk, SModel=People, Model_form=Zayavitel_people, redir='person', title='Данные о персонах')

# добавление и редактирование адресов
def profile_adres_edit(request, pkk):
    return get_form(request=request, pkk=pkk, SModel=Adres, Model_form=Adres_form, redir='adres', title='Данные об адресах')

# добавление и редактирование юр.лица
def zayavitel_edit(request, pkk):
    return get_form(request, pkk, Zayavitel_ur, Zayavitel_form, 'zayavitel', 'Данные о заявителе')

# удаление людей
def profile_del(request, pkk):
    try:
        people1 = People.objects.get(pk=pkk, author=request.user)
        people1.delete()
    except People.DoesNotExist:
        people_nayden = False
    return redirect('person')

# удаление адресов
def profile_adres_del(request, pkk):
    try:
        people1 = Adres.objects.get(pk=pkk, author=request.user)
        people1.delete()
    except Adres.DoesNotExist:
        people_nayden = False
    return redirect('adres')

# удаление юр.лица
def zayavitel_del(request, pkk):
    try:
        item = Zayavitel_ur.objects.get(pk=pkk, author=request.user)
        item.delete()
    except Zayavitel_ur.DoesNotExist:
        people_nayden = False
    return redirect('zayavitel')

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
def profile_view(request):
    fio = People.objects.filter(author=request.user)
    return render(request, 'lkk/profile_view.html', {'fio': fio, 'title' : 'Персоны'})

# просмотр списка адресов
def profile_adres(request):
    adres = Adres.objects.filter(author=request.user)
    return render(request, 'lkk/profile_adres_view.html', {'adres': adres, 'title': 'Адреса'})

# просмотр списка юр.лиц
def zayavitel(request):
    zaya = Zayavitel_ur.objects.filter(author=request.user)
    return render(request, 'lkk/profile_zayavitel_view.html', {'zaya': zaya, 'title': 'Заявители', 'user': request.user})

# просмотр списка заявок
def zayavka_view(request):
    zaya = Zayavka.objects.filter(author=request.user)
    return render(request, 'lkk/profile_zayavka_view.html', {'zaya': zaya, 'title': 'Заявки на технологическое присоединение',
                                                             'user': request.user})
# Вывод главной страницы ЛКК
def main_lk(request):
    return render(request, 'lkk/main.html')