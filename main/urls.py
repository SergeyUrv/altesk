from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),

    path('o_nas/kontakty', views.o_nas_kontakty.as_view(), name='o_nas_kontakty'),

    path('o_nas/rekvizity', views.o_nas_rekvizity.as_view(), name='o_nas_rekvizity'),

    path('raskrytie_informacii/godovaya_finansovaya_otchetnost',
         views.raskr_inf_godovaya_finansovaya_otchetnost.as_view(),
         name='raskr_inf_godovaya_finansovaya_otchetnost'),

    path('raskrytie_informacii/struktura_i_obem_zatrat',
         views.raskr_inf_struktura_i_obem_zatrat.as_view(),
         name='raskr_inf_struktura_i_obem_zatrat'),

    path('raskrytie_informacii/metod_dohodnosti_investirovannogo_kapitala',
         views.raskr_inf_metod_dohodnosti_investirovannogo_kapitala.as_view(),
         name='raskr_inf_metod_dohodnosti_investirovannogo_kapitala'),

    path('raskrytie_informacii/predlozheniya_o_razmere_cen',
         views.raskr_inf_predlozheniya_o_razmere_cen.as_view(),
         name='raskr_inf_predlozheniya_o_razmere_cen'),

    path('raskrytie_informacii/o_cenah_na_tovary_raboty_i_uslugi',
         views.raskr_inf_o_cenah_na_tovary_raboty_i_uslugi.as_view(),
         name='raskr_inf_o_cenah_na_tovary_raboty_i_uslugi'),

    path(
        'raskrytie_informacii/o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie',
        views.raskr_inf_o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie.as_view(),
        name='raskr_inf_o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie'),

    path(
        'raskrytie_informacii/o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva',
        views.raskr_inf_o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva.as_view(),
        name='raskr_inf_o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva'),

    path('raskrytie_informacii/ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug',
         views.raskr_inf_ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug.as_view(),
         name='raskr_inf_ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug'),

    path('raskrytie_informacii/o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam',
         views.raskr_inf_o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam.as_view(),
         name='raskr_inf_o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam'),

    path('raskrytie_informacii/o_velichine_rezerviruemoj_maksimalnoj_moshchnosti',
         views.raskr_inf_o_velichine_rezerviruemoj_maksimalnoj_moshchnosti.as_view(),
         name='raskr_inf_o_velichine_rezerviruemoj_maksimalnoj_moshchnosti'),

    path('raskrytie_informacii/o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov',
         views.raskr_inf_o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov.as_view(),
         name='raskr_inf_o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov'),

    path('raskrytie_informacii/ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug',
         views.raskr_inf_ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug.as_view(),
         name='raskr_inf_ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug'),

    path(
        'raskrytie_informacii/o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem',
        views.raskr_inf_o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem.as_view(),
        name='raskr_inf_o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem'),

    path('raskrytie_informacii/o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya',
         views.raskr_inf_o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya.as_view(),
         name='raskr_inf_o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya'),

    path('raskrytie_informacii/ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie',
         views.raskr_inf_ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie.as_view(),
         name='raskr_inf_ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie'),

    path('raskrytie_informacii/ob_investicionnyh_programmah',
         views.raskr_inf_ob_investicionnyh_programmah.as_view(),
         name='raskr_inf_ob_investicionnyh_programmah'),

    path('raskrytie_informacii/ob_otchetah_o_realizacii_investicionnyh_programm',
         views.raskr_inf_ob_otchetah_o_realizacii_investicionnyh_programm.as_view(),
         name='raskr_inf_ob_otchetah_o_realizacii_investicionnyh_programm'),

    path(
        'raskrytie_informacii/o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii',
        views.raskr_inf_o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii.as_view(),
        name='raskr_inf_o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii'),

    path('raskrytie_informacii/o_pasportah_uslug',
         views.raskr_inf_o_pasportah_uslug.as_view(),
         name='raskr_inf_o_pasportah_uslug'),

    path('raskrytie_informacii/o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost',
         views.raskr_inf_o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost.as_view(),
         name='raskr_inf_o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost'),

    path('raskrytie_informacii/o_kachestve_obsluzhivaniya_potrebitelej_uslug',
         views.raskr_inf_o_kachestve_obsluzhivaniya_potrebitelej_uslug.as_view(),
         name='raskr_inf_o_kachestve_obsluzhivaniya_potrebitelej_uslug'),

    path(
        'raskrytie_informacii/ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter',
        views.raskr_inf_ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter.as_view(),
        name='raskr_inf_ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter'),

    path('raskrytie_informacii/o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty',
         views.raskr_inf_o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty.as_view(),
         name='raskr_inf_o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty'),

    path('potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/obshchaya_informaciya',
         views.potr_ter_obsl_so_obshchaya_informaciya.as_view(),
         name='potr_ter_obsl_so_obshchaya_informaciya'),

    path('potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/tekhnicheskoe_sostoyanie_setej',
         views.potr_ter_obsl_so_tekhnicheskoe_sostoyanie_setej.as_view(),
         name='potr_ter_obsl_so_tekhnicheskoe_sostoyanie_setej'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/obshchaya_informaciya_o_peredache_elektricheskoj_energii',
         views.potr_peredacha_ee_obshchaya_informaciya_o_peredache_elektricheskoj_energii.as_view(),
         name='potr_peredacha_ee_obshchaya_informaciya_o_peredache_elektricheskoj_energii'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/normativnye_dokumenty',
         views.potr_peredacha_ee_normativnye_dokumenty.as_view(),
         name='potr_peredacha_ee_normativnye_dokumenty'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/pasporta_uslug_processov',
         views.potr_peredacha_ee_pasporta_uslug_processov.as_view(),
         name='potr_peredacha_ee_pasporta_uslug_processov'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/tipovye_formy_dokumentov',
         views.potr_peredacha_ee_tipovye_formy_dokumentov.as_view(),
         name='potr_peredacha_ee_tipovye_formy_dokumentov'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/tarify_na_uslugi_po_peredache_elektricheskoj_energii',
         views.potr_peredacha_ee_tarify_na_uslugi_po_peredache_elektricheskoj_energii.as_view(),
         name='potr_peredacha_ee_tarify_na_uslugi_po_peredache_elektricheskoj_energii'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/balans_elektricheskoj_energii_i_moshchnosti',
         views.potr_peredacha_ee_balans_elektricheskoj_energii_i_moshchnosti.as_view(),
         name='potr_peredacha_ee_balans_elektricheskoj_energii_i_moshchnosti'),

    path('potrebitelyam/peredacha_elektricheskoj_energii/zatraty_na_oplatu_poter',
         views.potr_peredacha_ee_zatraty_na_oplatu_poter.as_view(),
         name='potr_peredacha_ee_zatraty_na_oplatu_poter'),

    path('potrebitelyam/tekhnologicheskoe_prisoedinenie/obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii',
         views.potr_tp_obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii.as_view(),
         name='potr_tp_obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii'),

    path('potrebitelyam/tekhnologicheskoe_prisoedinenie/normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii',
         views.potr_tp_normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii.as_view(),
         name='potr_tp_normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii'),

    path(
        'potrebitelyam/tekhnologicheskoe_prisoedinenie/pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii',
        views.potr_tp_pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii.as_view(),
        name='potr_tp_pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii'),

    path(
        'potrebitelyam/tekhnologicheskoe_prisoedinenie/poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam',
        views.potr_tp_poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam.as_view(),
        name='potr_tp_poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam'),

    path(
        'potrebitelyam/tekhnologicheskoe_prisoedinenie/tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii',
        views.potr_tp_tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii.as_view(),
        name='potr_tp_tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii'),

    path('potrebitelyam/tekhnologicheskoe_prisoedinenie/tarify_na_tekhnologicheskoe_prisoedinenie',
         views.potr_tp_tarify_na_tekhnologicheskoe_prisoedinenie.as_view(),
         name='potr_tp_tarify_na_tekhnologicheskoe_prisoedinenie'),

    path(
        'potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_nalichii_moshchnosti_svobodnoj_dlya_tekhnologicheskogo_prisoedineniya',
        views.potr_tp_svedeniya_o_nalichii_moshchnosti.as_view(),
        name='potr_tp_svedeniya_o_nalichii_moshchnosti'),

    path(
        'potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_podannyh_zayavkah_na_tekhnologicheskoe_prisoedinenie_zaklyuchennyh_dogovorah_i_vypolnennyh_prisoedineniyah',
        views.potr_tp_svedeniya_o_podannyh_zayavkah_na_tp.as_view(),
        name='potr_tp_svedeniya_o_podannyh_zayavkah_na_tp'),

    path(
        'potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/obshchaya_informaciya_o_kommercheskom_uchete_elektricheskoj_energii',
        views.potr_kom_uchet_ee_obshchaya_informaciya.as_view(),
        name='potr_kom_uchet_ee_obshchaya_informaciya'),

    path(
        'potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/normativnye_dokumenty_o_kommercheskom_uchete_elektricheskoj_energii',
        views.potr_kom_uchet_ee_normativnye_dokumenty.as_view(),
        name='potr_kom_uchet_ee_obshchaya_normativnye_dokumenty'),

    path(
        'potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/pasporta_processov_o_kommercheskom_uchete_elektricheskoj_energii',
        views.potr_kom_uchet_ee_pasporta_processov.as_view(),
        name='potr_kom_uchet_ee_obshchaya_pasporta_processov'),

    path(
        'potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/tipovye_formy_dokumentov_o_kommercheskom_uchete_elektricheskoj_energii',
        views.potr_kom_uchet_ee_tipovye_formy_dokumentov.as_view(),
        name='potr_kom_uchet_ee_obshchaya_tipovye_formy_dokumentov'),

    path('potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/trebovaniya_k_organizacii_ucheta',
         views.potr_kom_uchet_ee_trebovaniya_k_organizacii_ucheta.as_view(),
         name='potr_kom_uchet_ee_obshchaya_trebovaniya_k_organizacii_ucheta'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/ofisy_obsluzhivaniya_potrebitelej',
         views.obsl_potr_ofisy_obsluzhivaniya_potrebitelej.as_view(),
         name='obsl_potr_ofisy_obsluzhivaniya_potrebitelej'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi',
         views.obsl_potr_zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi.as_view(),
         name='obsl_potr_zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/interaktivnaya_obratnaya_svyaz',
         views.obsl_potr_interaktivnaya_obratnaya_svyaz.as_view(),
         name='obsl_potr_interaktivnaya_obratnaya_svyaz'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej',
         views.obsl_potr_normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej.as_view(),
         name='obsl_potr_normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/lichnyj_kabinet_potrebitelya',
         views.obsl_potr_lichnyj_kabinet_potrebitelya.as_view(),
         name='obsl_potr_lichnyj_kabinet_potrebitelya'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/voprosy_i_otvety',
         views.obsl_potr_voprosy_i_otvety.as_view(),
         name='obsl_potr_voprosy_i_otvety'),

]
