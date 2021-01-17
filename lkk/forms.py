from django import forms

from .models import Eso, Zayavka, Zayavitel_ur, Adres, People, Doc_ur
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ZayavkaForm(forms.ModelForm):
    #error_css_class = 'valid-feedback'
    #required_css_class = 'invalid-feedback'

    class Meta:
        model = Zayavka
        fields = ('__all__')
        exclude = ('created_date', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Сохранить', 'Сохранить'))
        for item in self.fields :
            if self.fields[item].required :
                self.fields[item].label = self.fields[item].label + '<i class="bi bi-exclamation" style="color: red;"></i>'
        #self.fields['prichina_obr'].widget.attrs.update(style="display: none")
        #self.fields['prichina_obr'].widget.label.attrs.update(style="display:None")


class Zayavitel_yur(forms.ModelForm):
    class Meta:
        model = Zayavitel_ur
        fields = ('__all__')
        exclude = ('created_date', 'author', )

class Zayavitel_people(forms.ModelForm):
    class Meta:
        model = People
        fields = ('__all__')
        exclude = ('created_date', 'author', 'cont_tel_podtverzden', 'cont_email_podtverzden')