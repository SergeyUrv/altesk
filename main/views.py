from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import ContentMain, ContentPotr, ContentRaskrInf, ContentFile


class index(View):
    @staticmethod
    def get(request):
        content = ContentMain.objects.get(name="Главная")
        content_photos = content.contentfile_set.all()
        return render(request, "main/index.html", {"content": content, "content_photos": content_photos})


class kontakty_i_rekvizity(View):
    @staticmethod
    def get(request):
        content = ContentMain.objects.get(name="Контакты и реквизиты")
        return render(request, "main/simple_page.html", {"content": content})


class karta_sajta(View):
    @staticmethod
    def get(request):
        content = ContentMain.objects.get(name="Карта сайта")
        return render(request, "main/site_map.html", {"content": content})


class raskr_inf_godovaya_finansovaya_otchetnost(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Годовая финансовая (бухгалтерская) отчетность")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_struktura_i_obem_zatrat(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Структура и объем затрат")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_metod_dohodnosti_investirovannogo_kapitala(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Метод доходности инвестированного капитала")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_predlozheniya_o_razmere_cen(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Предложения о размере цен (тарифов)")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_investicionnye_programmy(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Инвестиционные программы")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_otchety_o_realizacii_investicionnyh_programm(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Отчеты о реализации инвестиционных программ")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_priobretenii_tovarov_dlya_okazaniya_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Способы приобретения, стоимость и объемы товаров, необходимых для оказания услуг по передаче электроэнергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_peredacha_ee_tarify_na_uslugi_po_peredache_elektroenergii(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Тарифы на услуги о передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_peredacha_ee_osnovnye_potrebitelskie_harakteristiki(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Основные потребительские характеристики передачи электроэнергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_peredacha_ee_usloviya_postavki_reguliruemyh_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Условиях, на которых осуществляется оказание услуг по передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_peredacha_ee_pasporta_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Паспорта услуг по передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_peredacha_ee_obem_i_stoimost_poter(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Объем и стоимость электрической энергии (мощности) за расчетный период, приобретенной в целях компенсации потерь")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_tp_tarify_na_tekhnologicheskoe_prisoedinenie(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Тарифы на технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_raskhody_na_tekhnologicheskoe_prisoedinenie_ne_vklyuchaemye_v_platu(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Расходы, связанные с осуществлением технологического присоединения, не включаемые в плату за технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_raskhody_na_stroitelstvo_obektov_elektrosetevogo_hozyajstva(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Расходы на строительство введенных в эксплуатацию объектов электросетевого хозяйства")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_tp_osnovnye_potrebitelskie_harakteristiki(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Основные потребительские характеристики технологиечского присоединения")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_dostup_k_reguliruemym_uslugam(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Наличие (отсутствие) технической возможности доступа к регулируемым товарам, работам и услугам")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_velichina_rezerviruemoj_maksimalnoj_moshchnosti(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Величина резервируемой максимальной мощности")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_rezultaty_kontrolnyh_zamerov(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Результаты контрольных замеров электрических параметров")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_tp_usloviya_postavki_reguliruemyh_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Условия, на которых осуществляется технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_poryadok_vypolneniya_tekhnologicheskih_tekhnicheskih(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Порядок выполнения технологических, технических и других мероприятий, связанных с технологическим присоединением")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_vozmozhnost_tekhnologicheskogo_prisoedineniya(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(
            name="Возможность подачи заявки на осуществление технологического присоединения")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_osnovnye_etapi_tekhnologicheskogo_prisoedineniya(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Основные этапы обработки заявок на технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_tp_pasporta_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Паспорта услуг по технологическому присоединению")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_lica_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Лица, намеревающиеся перераспределить максимальную мощность")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_kachestvo_obsluzhivaniya_potrebitelej_uslug(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Качество обслуживания потребителей услуг")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class raskr_inf_vydelennye_abonentskih_nomerah(View):
    @staticmethod
    def get(request):
        content = ContentRaskrInf.objects.get(name="Выделенные абонентские номера и адреса электронной почты")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_ter_obsl_so_obshchaya_informaciya(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Общая информация о территории обслуживания сетевой организации")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_ter_obsl_so_tekhnicheskoe_sostoyanie_setej(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Техническое состояние сетей")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_obshchaya_informaciya_o_peredache_elektricheskoj_energii(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Общая информация о передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_normativnye_dokumenty(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Нормативные документы о передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_pasporta_uslug_processov(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Паспорта услуг (процессов) по передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_tipovye_formy_dokumentov(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Типовые формы документов по передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_tarify_na_uslugi_po_peredache_elektricheskoj_energii(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Тарифы на услуги по передаче электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_balans_elektricheskoj_energii_i_moshchnosti(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Баланс электрической энергии и мощности")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_peredacha_ee_zatraty_na_oplatu_poter(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Затраты на оплату потерь")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Общая информация о технологическом присоединении")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Нормативные документы о технологическом присоединении")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Паспорта услуг (процессов) технологического присоединения")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Порядок выполнения мероприятий, связанных с присоединением к сетям")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii(View):
    def get(self, request):
        content = ContentPotr.objects.get(name="Типовые формы документов на технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_tarify_na_tekhnologicheskoe_prisoedinenie(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Тарифы на технологическое присоединение")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_svedeniya_o_nalichii_moshchnosti(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(
            name="Сведения о наличии мощности, свободной для технологического присоединения")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_tp_svedeniya_o_podannyh_zayavkah_na_tp(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(
            name="Сведения о поданных заявках на технологическое присоединение, заключенных договорах и выполненных присоединениях")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_kom_uchet_ee_obshchaya_informaciya(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Общая информация о коммерческом учете электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_kom_uchet_ee_normativnye_dokumenty(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Нормативные документы о коммерческом учете электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_kom_uchet_ee_pasporta_processov(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Паспорта процессов коммерческого учета электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_kom_uchet_ee_tipovye_formy_dokumentov(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Типовые формы документов коммерческого учета электрической энергии")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class potr_kom_uchet_ee_trebovaniya_k_organizacii_ucheta(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Требования к организации учета")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_ofisy_obsluzhivaniya_potrebitelej(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Офисы обслуживания потребителей")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(
            name="Заочное обслуживание посредством телефонной связи (Единый центр обработки вызовов)")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_interaktivnaya_obratnaya_svyaz(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Интерактивная обратная связь (интернет-приемная)")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Нормативные документы по обслуживанию потребителей")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_lichnyj_kabinet_potrebitelya(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Личный кабинет потребителя")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})


class obsl_potr_voprosy_i_otvety(View):
    @staticmethod
    def get(request):
        content = ContentPotr.objects.get(name="Вопросы и ответы")
        content_files = content.contentfile_set.order_by('-date_year', '-date_quarter', '-date_month')
        return render(request, "main/simple_page.html",
                      {"content": content, "content_files": content_files})
