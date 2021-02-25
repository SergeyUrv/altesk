from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Content, ContentFile


class index(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Главная")
        return render(request, "main/simple_page.html", {"content": content})


class o_nas_kontakty(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Контакты")
        return render(request, "main/simple_page.html", {"content": content})


class o_nas_rekvizity(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Реквизиты")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_godovaya_finansovaya_otchetnost(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Годовая финансовая (бухгалтерская) отчетность")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_struktura_i_obem_zatrat(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Структура и объем затрат")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_metod_dohodnosti_investirovannogo_kapitala(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Метод доходности инвестированного капитала")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_predlozheniya_o_razmere_cen(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Предложения о размере цен (тарифов)")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_cenah_na_tovary_raboty_i_uslugi(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О ценах (тарифах) на товары, работы и услуги")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie(
    View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О расходах, связанных с осуществлением технологического присоединения, не включаемых в плату за технологическое присоединение")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О расходах на строительство введенных в эксплуатацию объектов электросетевого хозяйства")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="Об основных потребительских характеристиках регулируемых товаров, работ и услуг")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О наличии (об отсутствии) технической возможности доступа к регулируемым товарам, работам и услугам")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_velichine_rezerviruemoj_maksimalnoj_moshchnosti(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О величине резервируемой максимальной мощности")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О результатах контрольных замеров электрических параметров")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="Об условиях, на которых осуществляется поставка регулируемых товаров, работ и услуг")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem(
    View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О порядке выполнения технологических, технических и других мероприятий, связанных с технологическим присоединением")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О возможности подачи заявки на осуществление технологического присоединения")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Об основных этапах обработки заявок на технологическое присоединение")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_investicionnyh_programmah(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Об инвестиционных программах")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_otchetah_o_realizacii_investicionnyh_programm(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Об отчетах о реализации инвестиционных программ")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii(
    View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="О способах приобретения, стоимости и об объемах товаров, необходимых для оказания услуг по передаче электроэнергии")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_pasportah_uslug(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О паспортах услуг (процессов)")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О лицах, намеревающихся перераспределить максимальную мощность")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_kachestve_obsluzhivaniya_potrebitelej_uslug(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О качестве обслуживания потребителей услуг")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter(
    View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="Об объеме и о стоимости электрической энергии (мощности) за расчетный период, приобретенной в целях компенсации потерь")
        return render(request, "main/simple_page.html", {"content": content})


class raskr_inf_o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="О выделенных абонентских номерах и адресах электронной почты")
        return render(request, "main/simple_page.html", {"content": content})


class potr_ter_obsl_so_obshchaya_informaciya(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Общая информация о территории обслуживания сетевой организации")
        return render(request, "main/simple_page.html", {"content": content})


class potr_ter_obsl_so_tekhnicheskoe_sostoyanie_setej(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Техническое состояние сетей")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_obshchaya_informaciya_o_peredache_elektricheskoj_energii(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Общая информация о передаче электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_normativnye_dokumenty(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Нормативные документы о передаче электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_pasporta_uslug_processov(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Паспорта услуг (процессов) по передаче электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_tipovye_formy_dokumentov(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Типовые формы документов по передаче электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_tarify_na_uslugi_po_peredache_elektricheskoj_energii(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Тарифы на услуги по передаче электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_balans_elektricheskoj_energii_i_moshchnosti(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Баланс электрической энергии и мощности")
        return render(request, "main/simple_page.html", {"content": content})


class potr_peredacha_ee_zatraty_na_oplatu_poter(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Затраты на оплату потерь")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Общая информация о технологическом присоединении")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Нормативные документы о технологическом присоединении")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Паспорта услуг (процессов) технологического присоединения")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Порядок выполнения мероприятий, связанных с присоединением к сетям")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii(View):
    def get(self, request):
        content = Content.objects.get(name="Типовые формы документов на технологическое присоединение")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_tarify_na_tekhnologicheskoe_prisoedinenie(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Тарифы на технологическое присоединение")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_svedeniya_o_nalichii_moshchnosti(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Сведения о наличии мощности, свободной для технологического присоединения")
        return render(request, "main/simple_page.html", {"content": content})


class potr_tp_svedeniya_o_podannyh_zayavkah_na_tp(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="Сведения о поданных заявках на технологическое присоединение, заключенных договорах и выполненных присоединениях")
        return render(request, "main/simple_page.html", {"content": content})


class potr_kom_uchet_ee_obshchaya_informaciya(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Общая информация о коммерческом учете электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_kom_uchet_ee_normativnye_dokumenty(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Нормативные документы о коммерческом учете электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_kom_uchet_ee_pasporta_processov(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Паспорта процессов коммерческого учета электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_kom_uchet_ee_tipovye_formy_dokumentov(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Типовые формы документов коммерческого учета электрической энергии")
        return render(request, "main/simple_page.html", {"content": content})


class potr_kom_uchet_ee_trebovaniya_k_organizacii_ucheta(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Требования к организации учета")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_ofisy_obsluzhivaniya_potrebitelej(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Офисы обслуживания потребителей")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(
            name="Заочное обслуживание посредством телефонной связи (Единый центр обработки вызовов)")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_interaktivnaya_obratnaya_svyaz(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Интерактивная обратная связь (интернет-приемная)")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Нормативные документы по обслуживанию потребителей")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_lichnyj_kabinet_potrebitelya(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Личный кабинет потребителя")
        return render(request, "main/simple_page.html", {"content": content})


class obsl_potr_voprosy_i_otvety(View):
    @staticmethod
    def get(request):
        content = Content.objects.get(name="Вопросы и ответы")
        return render(request, "main/simple_page.html", {"content": content})
