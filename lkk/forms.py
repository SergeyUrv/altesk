from django import forms

from .models import Eso, Zayavka, Zayavitel_ur, Adres, People
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.urls import reverse

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не корректны.')
        return cd['password2']

#форма подачи заявки на тех присоединение
class ZayavkaForm(forms.ModelForm):
    #error_css_class = 'valid-feedback'
    #required_css_class = 'invalid-feedback'

    class Meta:
        model = Zayavka
        #fields = ('__all__')
        exclude = ('created_date', 'author', 'status', 'status_date', 'status_error', 'zaya_file')

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(ZayavkaForm, self).__init__(*args, **kwargs)
        #обрабатываем списки, выдаем только значения созданные пользователем
        i = Zayavitel_ur.objects.filter(author=user_id)
        self.fields['org'].queryset = i
        i = People.objects.filter(author=user_id)
        self.fields['fio'].queryset = i
        i = Adres.objects.filter(author=user_id)
        self.fields['mestopolozenie_ustroystv'].queryset = i

        #добавляем кнопочку сохранить
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Сохранить', 'Сохранить'))
        #добавляем кнопочки добавить
        for item in self.fields :
            if self.fields[item].required :
                self.fields[item].label = self.fields[item].label + '<i class="bi bi-exclamation" style="color: red;"></i>'
            if item == 'fio' :
                self.fields[item].label = self.fields[item].label + '<a href="'+ reverse('person_edit', args='0') + '", title="Добавить..."><i class="bi bi-person-plus-fill"></i></a>'
            if item == 'org':
                self.fields[item].label = self.fields[item].label +\
                                          '<a href="' + reverse('zayavitel_edit',args='0') +\
                                          '", title="Добавить..."><i class="bi bi-building"></i></a>'
        #self.fields['prichina_obr'].widget.attrs.update(style="display: none")
        #self.fields['prichina_obr'].widget.label.attrs.update(style="display:None")


class Zayavitel_yur(forms.ModelForm):
    class Meta:
        model = Zayavitel_ur
        #fields = ('__all__')
        exclude = ('created_date', 'author', )

class Zayavitel_people(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Zayavitel_people, self).__init__(*args, **kwargs)
        i=Adres.objects.filter(author=user_id)
        self.fields['adr_main'].queryset = i
        self.fields['adr_post'].queryset = i
        self.fields['adr_fakt'].queryset = i
    class Meta:
        model = People
        #fields = ('__all__')
        exclude = ('created_date', 'author', 'cont_tel_podtverzden', 'cont_email_podtverzden')

class Adres_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Adres_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Adres
        #fields = ('__all__')
        exclude = ('created_date', 'author', )

class Zayavitel_form(forms.ModelForm):
    #делаем, чтобы в списке выбора были только созданные пользователем значения
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Zayavitel_form, self).__init__(*args, **kwargs)
        i=Adres.objects.filter(author=user_id)
        self.fields['adr_ur'].queryset = i
        self.fields['adr_post'].queryset = i
        self.fields['adr_fakt'].queryset = i
        i=People.objects.filter(author=user_id, people_type='ruk')
        #self.fields['fio'].queryset = i
        self.fields['ruk_fio'].queryset = i
        i = People.objects.filter(author=user_id, people_type='pre')
        self.fields['pred_fio'].queryset = i

    #pred_document_date = DateField(widget=AdminDateWidget)

    class Meta:
        model = Zayavitel_ur
        #fields = ('__all__')
        exclude = ('created_date', 'author', )
        labels = {
            'fio': 'ФИО заявителя <a href="/lk/profile_fio/edit/0", title="Добавить..."><i class="bi bi-person-plus-fill"></i></a>',
            'ruk_fio':'ФИО руководителя <a href="/lk/profile_fio/edit/0", title="Добавить..."><i class="bi bi-person-plus-fill"></i></a>',
            'pred_fio': 'ФИО представителя <a href="/lk/profile_fio/edit/0", title="Добавить..."><i class="bi bi-person-plus-fill"></i></a>',
            'adr_ur': 'Юридический адрес <a href="/lk/profile_adres/edit/0", title="Добавить..."><i class="bi bi-globe"></i></a>',
            'adr_post': 'Почтовый адрес <a href="/lk/profile_adres/edit/0", title="Добавить..."><i class="bi bi-globe"></i></a>',
            'adr_fakt': 'Фактический адрес <a href="/lk/profile_adres/edit/0", title="Добавить..."><i class="bi bi-globe"></i></a>',
        }