from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),

    path('kontakty_i_rekvizity', views.kontakty_i_rekvizity.as_view(), name='kontakty_i_rekvizity'),

    path('karta_sajta', views.karta_sajta.as_view(), name='karta_sajta'),

    path('raskrytie_informacii/finansovaya_informaciya/godovaya_finansovaya_otchetnost',
         views.raskr_inf_godovaya_finansovaya_otchetnost.as_view(),
         name='raskr_inf_godovaya_finansovaya_otchetnost'),

    path('raskrytie_informacii/finansovaya_informaciya/struktura_i_obem_zatrat',
         views.raskr_inf_struktura_i_obem_zatrat.as_view(),
         name='raskr_inf_struktura_i_obem_zatrat'),

    path('raskrytie_informacii/finansovaya_informaciya/metod_dohodnosti_investirovannogo_kapitala',
         views.raskr_inf_metod_dohodnosti_investirovannogo_kapitala.as_view(),
         name='raskr_inf_metod_dohodnosti_investirovannogo_kapitala'),

    path('raskrytie_informacii/finansovaya_informaciya/predlozheniya_o_razmere_cen',
         views.raskr_inf_predlozheniya_o_razmere_cen.as_view(),
         name='raskr_inf_predlozheniya_o_razmere_cen'),

    path('raskrytie_informacii/finansovaya_informaciya/investicionnye_programmy',
         views.raskr_inf_investicionnye_programmy.as_view(),
         name='raskr_inf_investicionnye_programmy'),

    path('raskrytie_informacii/finansovaya_informaciya/otchety_o_realizacii_investicionnyh_programm',
         views.raskr_inf_otchety_o_realizacii_investicionnyh_programm.as_view(),
         name='raskr_inf_otchety_o_realizacii_investicionnyh_programm'),

    path(
        'raskrytie_informacii/finansovaya_informaciya/priobretenii_tovarov_dlya_okazaniya_uslug',
        views.raskr_inf_priobretenii_tovarov_dlya_okazaniya_uslug.as_view(),
        name='raskr_inf_priobretenii_tovarov_dlya_okazaniya_uslug'),

    path('raskrytie_informacii/peredacha_elektricheskoj_energii/tarify_na_uslugi_po_peredache_elektroenergii',
         views.raskr_inf_peredacha_ee_tarify_na_uslugi_po_peredache_elektroenergii.as_view(),
         name='raskr_inf_peredacha_ee_tarify_na_uslugi_po_peredache_elektroenergii'),

    path(
        'raskrytie_informacii/peredacha_elektricheskoj_energii/osnovnye_potrebitelskie_harakteristiki',
        views.raskr_inf_peredacha_ee_osnovnye_potrebitelskie_harakteristiki.as_view(),
        name='raskr_inf_peredacha_ee_osnovnye_potrebitelskie_harakteristiki'),

    path(
        'raskrytie_informacii/peredacha_elektricheskoj_energii/usloviya_postavki_reguliruemyh_uslug',
        views.raskr_inf_peredacha_ee_usloviya_postavki_reguliruemyh_uslug.as_view(),
        name='raskr_inf_peredacha_ee_usloviya_postavki_reguliruemyh_uslug'),

    path('raskrytie_informacii/peredacha_elektricheskoj_energii/pasporta_uslug',
         views.raskr_inf_peredacha_ee_pasporta_uslug.as_view(),
         name='raskr_inf_peredacha_ee_pasporta_uslug'),

    path(
        'raskrytie_informacii/peredacha_elektricheskoj_energii/obem_i_stoimost_poter',
        views.raskr_inf_peredacha_ee_obem_i_stoimost_poter.as_view(),
        name='raskr_inf_peredacha_ee_obem_i_stoimost_poter'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/tarify_na_tekhnologicheskoe_prisoedinenie',
         views.raskr_inf_tp_tarify_na_tekhnologicheskoe_prisoedinenie.as_view(),
         name='raskr_inf_tp_tarify_na_tekhnologicheskoe_prisoedinenie'),

    path(
        'raskrytie_informacii/tekhnologicheskoe_prisoedinenie/raskhody_na_tekhnologicheskoe_prisoedinenie_ne_vklyuchaemye_v_platu',
        views.raskr_inf_raskhody_na_tekhnologicheskoe_prisoedinenie_ne_vklyuchaemye_v_platu.as_view(),
        name='raskr_inf_raskhody_na_tekhnologicheskoe_prisoedinenie_ne_vklyuchaemye_v_platu'),

    path(
        'raskrytie_informacii/tekhnologicheskoe_prisoedinenie/raskhody_na_stroitelstvo_obektov_elektrosetevogo_hozyajstva',
        views.raskr_inf_raskhody_na_stroitelstvo_obektov_elektrosetevogo_hozyajstva.as_view(),
        name='raskr_inf_raskhody_na_stroitelstvo_obektov_elektrosetevogo_hozyajstva'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/osnovnye_potrebitelskie_harakteristiki',
         views.raskr_inf_tp_osnovnye_potrebitelskie_harakteristiki.as_view(),
         name='raskr_inf_tp_osnovnye_potrebitelskie_harakteristiki'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/dostup_k_reguliruemym_uslugam',
         views.raskr_inf_dostup_k_reguliruemym_uslugam.as_view(),
         name='raskr_inf_dostup_k_reguliruemym_uslugam'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/velichina_rezerviruemoj_maksimalnoj_moshchnosti',
         views.raskr_inf_velichina_rezerviruemoj_maksimalnoj_moshchnosti.as_view(),
         name='raskr_inf_velichina_rezerviruemoj_maksimalnoj_moshchnosti'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/rezultaty_kontrolnyh_zamerov',
         views.raskr_inf_rezultaty_kontrolnyh_zamerov.as_view(),
         name='raskr_inf_rezultaty_kontrolnyh_zamerov'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/usloviya_postavki_reguliruemyh_uslug',
         views.raskr_inf_tp_usloviya_postavki_reguliruemyh_uslug.as_view(),
         name='raskr_inf_tp_usloviya_postavki_reguliruemyh_uslug'),

    path(
        'raskrytie_informacii/tekhnologicheskoe_prisoedinenie/poryadok_vypolneniya_tekhnologicheskih_tekhnicheskih',
        views.raskr_inf_poryadok_vypolneniya_tekhnologicheskih_tekhnicheskih.as_view(),
        name='raskr_inf_poryadok_vypolneniya_tekhnologicheskih_tekhnicheskih'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/vozmozhnost_tekhnologicheskogo_prisoedineniya',
         views.raskr_inf_vozmozhnost_tekhnologicheskogo_prisoedineniya.as_view(),
         name='raskr_inf_vozmozhnost_tekhnologicheskogo_prisoedineniya'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/osnovnye_etapi_tekhnologicheskogo_prisoedineniya',
         views.raskr_inf_osnovnye_etapi_tekhnologicheskogo_prisoedineniya.as_view(),
         name='raskr_inf_osnovnye_etapi_tekhnologicheskogo_prisoedineniya'),

    path('raskrytie_informacii/tekhnologicheskoe_prisoedinenie/pasporta_uslug',
         views.raskr_inf_tp_pasporta_uslug.as_view(),
         name='raskr_inf_tp_pasporta_uslug'),

    path(
        'raskrytie_informacii/tekhnologicheskoe_prisoedinenie/lica_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost',
        views.raskr_inf_lica_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost.as_view(),
        name='raskr_inf_lica_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost'),

    path('raskrytie_informacii/kachestvo_obsluzhivaniya_potrebitelej_uslug',
         views.raskr_inf_kachestvo_obsluzhivaniya_potrebitelej_uslug.as_view(),
         name='raskr_inf_kachestvo_obsluzhivaniya_potrebitelej_uslug'),

    path('raskrytie_informacii/vydelennye_abonentskih_nomerah',
         views.raskr_inf_vydelennye_abonentskih_nomerah.as_view(),
         name='raskr_inf_vydelennye_abonentskih_nomerah'),

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

    # path('potrebitelyam/obsluzhivanie_potrebitelej/lichnyj_kabinet_potrebitelya',
    #      views.obsl_potr_lichnyj_kabinet_potrebitelya.as_view(),
    #      name='obsl_potr_lichnyj_kabinet_potrebitelya'),

    path('potrebitelyam/obsluzhivanie_potrebitelej/voprosy_i_otvety',
         views.obsl_potr_voprosy_i_otvety.as_view(),
         name='obsl_potr_voprosy_i_otvety'),

]
