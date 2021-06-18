from django import forms

from .models import Eso, Zayavka, Zayavitel_ur, Adres, People, Epu, Obracheniya, Zayavka_pu
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.urls import reverse

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_email(self):
        cd = self.cleaned_data
        if not cd['email']:
            raise forms.ValidationError('Введите email, иначе мы не сможем восстановить доступ к личному кабинету, если Вы забудите пароль.')
        return cd['email']

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
        exclude = ('created_date', 'author', 'status', 'status_date', 'status_error', 'zaya_file',
                   'admin_file_doc', 'admin_file_akttp', 'admin_file_doceso', 'admin_file_invoice', 'admin_file_aip',
                   'admin_comment')

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
        #добавляем кнопочки добавить
        for item in self.fields :
            if item == 'adr_main' or item == 'adr_post' or item == 'adr_fakt':
                self.fields[item].label = self.fields[item].label + '<a href="'+ reverse('adres_edit', args='0') +'", title="Добавить..."><i class="bi bi-globe"></i></a>'

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
        #добавляем кнопочки добавить
        for item in self.fields :
            if item == 'fio' or item == 'ruk_fio' or item == 'pred_fio' :
                self.fields[item].label = self.fields[item].label + '<a href="'+ reverse('person_edit', args='0') +'", title="Добавить..."><i class="bi bi-person-plus-fill"></i></a>'
            if item == 'adr_ur' or item == 'adr_post' or item == 'adr_fakt':
                self.fields[item].label = self.fields[item].label + '<a href="'+ reverse('adres_edit', args='0') +'", title="Добавить..."><i class="bi bi-globe"></i></a>'

    #pred_document_date = DateField(widget=AdminDateWidget)

    class Meta:
        model = Zayavitel_ur
        #fields = ('__all__')
        exclude = ('created_date', 'author', )

class Obracheniya_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Obracheniya_form, self).__init__(*args, **kwargs)
        #обрабатываем списки, выдаем только значения созданные пользователем
        i = Zayavitel_ur.objects.filter(author=user_id)
        self.fields['org'].queryset = i
        i = People.objects.filter(author=user_id)
        self.fields['fio'].queryset = i

    class Meta:
        model = Obracheniya
        #fields = ('__all__')
        exclude = ('created_date', 'author', 'status')

class Zayavka_pu_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Zayavka_pu_form, self).__init__(*args, **kwargs)
        #обрабатываем списки, выдаем только значения созданные пользователем
        i = Zayavitel_ur.objects.filter(author=user_id)
        self.fields['org'].queryset = i
        i = People.objects.filter(author=user_id)
        self.fields['fio'].queryset = i

    class Meta:
        model = Zayavka_pu
        #fields = ('__all__')
        exclude = ('created_date', 'author')

class Epu_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('users')
        super(Epu_form, self).__init__(*args, **kwargs)
        #обрабатываем списки, выдаем только значения созданные пользователем
        i = Adres.objects.filter(author=user_id)
        self.fields['epu_adres'].queryset = i

    class Meta:
        model = Epu
        #fields = ('__all__')
        exclude = ('created_date', 'author')

##### админ формы для заявок на тех прес.
#форма подачи заявки на тех присоединение
class ZayavkaForm_edit(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ('status_error', 'admin_comment', 'admin_file_doc', 'admin_file_invoice', 'admin_file_akttp', 'admin_file_aip', 'admin_file_doceso')
        # exclude = ('created_date', 'author', 'status', 'status_date', 'status_error', 'zaya_file',
        #            'admin_file_doc', 'admin_file_akttp', 'admin_file_doceso', 'admin_file_invoice', 'admin_file_aip',
        #            'admin_comment')

    def __init__(self, *args, **kwargs):
        status = kwargs.pop('status')
        eso = kwargs.pop('eso')
        super(ZayavkaForm_edit, self).__init__(*args, **kwargs)
        if status == 'edit':
            self.fields['admin_file_doc'].widget = forms.HiddenInput()
            self.fields['admin_file_invoice'].widget = forms.HiddenInput()
            self.fields['admin_file_akttp'].widget = forms.HiddenInput()
            self.fields['admin_file_aip'].widget = forms.HiddenInput()
            self.fields['admin_file_doceso'].widget = forms.HiddenInput()
        if status == 'obr':
            self.fields['status_error'].widget = forms.HiddenInput()
            self.fields['admin_file_akttp'].widget = forms.HiddenInput()
            self.fields['admin_file_aip'].widget = forms.HiddenInput()
            if eso:
                self.fields['admin_file_doceso'].widget = forms.HiddenInput()

        #добавляем кнопочку сохранить
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Сохранить', 'Сохранить'))

#форма подачи заявки на тех присоединение - приложить договор ЭСО
class ZayavkaForm_edit_eso(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ('admin_comment', 'admin_file_doceso')

    def __init__(self, *args, **kwargs):
        status = kwargs.pop('status')
        eso = kwargs.pop('eso')
        super(ZayavkaForm_edit_eso, self).__init__(*args, **kwargs)



