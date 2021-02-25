$('.ckcontent p').addClass('text-lg');

if (window.location.pathname === '/') {
    $("#glavnaya").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii') {
    $("#raskrytie_informacii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/o_nas/kontakty' ||
    window.location.pathname === '/o_nas/rekvizity') {
    $("#o_nas_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#o_nas_vision a").addClass('sidebar-link');
    $("#o_nas_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/o_nas/kontakty') {
    $("#kontakty").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/o_nas/rekvizity') {
    $("#rekvizity").addClass('sidebar-item active');
}
;


if (window.location.pathname === '/raskrytie_informacii/godovaya_finansovaya_otchetnost' ||
    window.location.pathname === '/raskrytie_informacii/struktura_i_obem_zatrat' ||
    window.location.pathname === '/raskrytie_informacii/metod_dohodnosti_investirovannogo_kapitala' ||
    window.location.pathname === '/raskrytie_informacii/predlozheniya_o_razmere_cen' ||
    window.location.pathname === '/raskrytie_informacii/o_cenah_na_tovary_raboty_i_uslugi' ||
    window.location.pathname === '/raskrytie_informacii/o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie' ||
    window.location.pathname === '/raskrytie_informacii/o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva' ||
    window.location.pathname === '/raskrytie_informacii/ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug' ||
    window.location.pathname === '/raskrytie_informacii/o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam' ||
    window.location.pathname === '/raskrytie_informacii/o_velichine_rezerviruemoj_maksimalnoj_moshchnosti' ||
    window.location.pathname === '/raskrytie_informacii/o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov' ||
    window.location.pathname === '/raskrytie_informacii/ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug' ||
    window.location.pathname === '/raskrytie_informacii/o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem' ||
    window.location.pathname === '/raskrytie_informacii/o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya' ||
    window.location.pathname === '/raskrytie_informacii/ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie' ||
    window.location.pathname === '/raskrytie_informacii/ob_investicionnyh_programmah' ||
    window.location.pathname === '/raskrytie_informacii/ob_otchetah_o_realizacii_investicionnyh_programm' ||
    window.location.pathname === '/raskrytie_informacii/o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii' ||
    window.location.pathname === '/raskrytie_informacii/o_pasportah_uslug' ||
    window.location.pathname === '/raskrytie_informacii/o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost' ||
    window.location.pathname === '/raskrytie_informacii/o_kachestve_obsluzhivaniya_potrebitelej_uslug' ||
    window.location.pathname === '/raskrytie_informacii/ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter' ||
    window.location.pathname === '/raskrytie_informacii/o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty') {
    $("#raskrytie_informacii_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#raskrytie_informacii_vision a").addClass('sidebar-link');
    $("#raskrytie_informacii_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/raskrytie_informacii/godovaya_finansovaya_otchetnost') {
    $("#godovaya_finansovaya_otchetnost").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/struktura_i_obem_zatrat') {
    $("#struktura_i_obem_zatrat").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/metod_dohodnosti_investirovannogo_kapitala') {
    $("#metod_dohodnosti_investirovannogo_kapitala").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/predlozheniya_o_razmere_cen') {
    $("#predlozheniya_o_razmere_cen").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_cenah_na_tovary_raboty_i_uslugi') {
    $("#o_cenah_na_tovary_raboty_i_uslugi").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie') {
    $("#o_raskhodah_svyazannyh_s_osushchestvleniem_tekhnologicheskogo_prisoedineniya_ne_vklyuchaemyh_v_platu_za_tekhnologicheskoe_prisoedinenie").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva') {
    $("#o_raskhodah_na_stroitelstvo_vvedennyh_v_ekspluataciyu_obektov_elektrosetevogo_hozyajstva").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug') {
    $("#ob_osnovnyh_potrebitelskih_harakteristikah_reguliruemyh_tovarov_rabot_i_uslug").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam') {
    $("#o_nalichii_tekhnicheskoj_vozmozhnosti_dostupa_k_reguliruemym_tovaram_rabotam_i_uslugam").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_velichine_rezerviruemoj_maksimalnoj_moshchnosti') {
    $("#o_velichine_rezerviruemoj_maksimalnoj_moshchnosti").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov') {
    $("#o_rezultatah_kontrolnyh_zamerov_elektricheskih_parametrov").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug') {
    $("#ob_usloviyah_na_kotoryh_osushchestvlyaetsya_postavka_reguliruemyh_tovarov_rabot_i_uslug").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem') {
    $("#o_poryadke_vypolneniya_tekhnologicheskih_tekhnicheskih_i_drugih_meropriyatij_svyazannyh_s_tekhnologicheskim_prisoedineniem").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya') {
    $("#o_vozmozhnosti_podachi_zayavki_na_osushchestvlenie_tekhnologicheskogo_prisoedineniya").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie') {
    $("#ob_osnovnyh_etapah_obrabotki_zayavok_na_tekhnologicheskoe_prisoedinenie").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_investicionnyh_programmah') {
    $("#ob_investicionnyh_programmah").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_otchetah_o_realizacii_investicionnyh_programm') {
    $("#ob_otchetah_o_realizacii_investicionnyh_programm").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii') {
    $("#o_sposobah_priobreteniya_stoimosti_i_ob_obemah_tovarov_neobhodimyh_dlya_okazaniya_uslug_po_peredache_elektroenergii").addClass('sidebar-item active');
}
;


if (window.location.pathname === '/raskrytie_informacii/o_pasportah_uslug') {
    $("#o_pasportah_uslug").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost') {
    $("#o_licah_namerevayushchihsya_pereraspredelit_maksimalnuyu_moshchnost").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_kachestve_obsluzhivaniya_potrebitelej_uslug') {
    $("#o_kachestve_obsluzhivaniya_potrebitelej_uslug").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter') {
    $("#ob_obeme_i_o_stoimosti_elektricheskoj_energii_za_raschetnyj_period_priobretennoj_v_celyah_kompensacii_poter").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/raskrytie_informacii/o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty') {
    $("#o_vydelennyh_abonentskih_nomerah_i_adresah_elektronnoj_pochty").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/tekhnicheskoe_sostoyanie_setej' ||
    window.location.pathname === '/potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/obshchaya_informaciya') {
    $("#territoriya_obsluzhivaniya_setevoj_organizacii_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#territoriya_obsluzhivaniya_setevoj_organizacii_vision a").addClass('sidebar-link');
    $("#territoriya_obsluzhivaniya_setevoj_organizacii_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/tekhnicheskoe_sostoyanie_setej') {
    $("#tekhnicheskoe_sostoyanie_setej").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/territoriya_obsluzhivaniya_setevoj_organizacii/obshchaya_informaciya') {
    $("#obshchaya_informaciya").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/obshchaya_informaciya_o_peredache_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/normativnye_dokumenty' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/pasporta_uslug_processov' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/tipovye_formy_dokumentov' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/tarify_na_uslugi_po_peredache_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/balans_elektricheskoj_energii_i_moshchnosti' ||
    window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/zatraty_na_oplatu_poter') {
    $("#peredacha_elektricheskoj_energii_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#peredacha_elektricheskoj_energii_vision a").addClass('sidebar-link');
    $("#peredacha_elektricheskoj_energii_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/obshchaya_informaciya_o_peredache_elektricheskoj_energii') {
    $("#obshchaya_informaciya_o_peredache_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/normativnye_dokumenty') {
    $("#normativnye_dokumenty").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/pasporta_uslug_processov') {
    $("#pasporta_uslug_processov").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/tipovye_formy_dokumentov') {
    $("#tipovye_formy_dokumentov").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/tarify_na_uslugi_po_peredache_elektricheskoj_energii') {
    $("#tarify_na_uslugi_po_peredache_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/balans_elektricheskoj_energii_i_moshchnosti') {
    $("#balans_elektricheskoj_energii_i_moshchnosti").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/peredacha_elektricheskoj_energii/zatraty_na_oplatu_poter') {
    $("#zatraty_na_oplatu_poter").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/tarify_na_tekhnologicheskoe_prisoedinenie' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_nalichii_moshchnosti_svobodnoj_dlya_tekhnologicheskogo_prisoedineniya' ||
    window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_podannyh_zayavkah_na_tekhnologicheskoe_prisoedinenie_zaklyuchennyh_dogovorah_i_vypolnennyh_prisoedineniyah') {
    $("#tekhnologicheskoe_prisoedinenie_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#tekhnologicheskoe_prisoedinenie_vision a").addClass('sidebar-link');
    $("#tekhnologicheskoe_prisoedinenie_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii') {
    $("#obshchaya_informaciya_o_tekhnologicheskom_prisoedinenii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii') {
    $("#normativnye_dokumenty_o_tekhnologicheskom_prisoedinenii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii') {
    $("#pasporta_uslug_processov_o_tekhnologicheskom_prisoedinenii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam_o_tekhnologicheskom_prisoedinenii') {
    $("#poryadok_vypolneniya_meropriyatij_svyazannyh_s_prisoedineniem_k_setyam_o_tekhnologicheskom_prisoedinenii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii') {
    $("#tipovye_formy_dokumentov_o_tekhnologicheskom_prisoedinenii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/tarify_na_tekhnologicheskoe_prisoedinenie') {
    $("#tarify_na_tekhnologicheskoe_prisoedinenie").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_nalichii_moshchnosti_svobodnoj_dlya_tekhnologicheskogo_prisoedineniya') {
    $("#svedeniya_o_nalichii_moshchnosti_svobodnoj_dlya_tekhnologicheskogo_prisoedineniya").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/tekhnologicheskoe_prisoedinenie/svedeniya_o_podannyh_zayavkah_na_tekhnologicheskoe_prisoedinenie_zaklyuchennyh_dogovorah_i_vypolnennyh_prisoedineniyah') {
    $("#svedeniya_o_podannyh_zayavkah_na_tekhnologicheskoe_prisoedinenie_zaklyuchennyh_dogovorah_i_vypolnennyh_prisoedineniyah").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/obshchaya_informaciya_o_kommercheskom_uchete_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/normativnye_dokumenty_o_kommercheskom_uchete_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/pasporta_processov_o_kommercheskom_uchete_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/tipovye_formy_dokumentov_o_kommercheskom_uchete_elektricheskoj_energii' ||
    window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/trebovaniya_k_organizacii_ucheta') {
    $("#kommercheskij_uchet_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#kommercheskij_uchet_vision a").addClass('sidebar-link');
    $("#kommercheskij_uchet_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/obshchaya_informaciya_o_kommercheskom_uchete_elektricheskoj_energii') {
    $("#obshchaya_informaciya_o_kommercheskom_uchete_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/normativnye_dokumenty_o_kommercheskom_uchete_elektricheskoj_energii') {
    $("#normativnye_dokumenty_o_kommercheskom_uchete_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/pasporta_processov_o_kommercheskom_uchete_elektricheskoj_energii') {
    $("#pasporta_processov_o_kommercheskom_uchete_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/tipovye_formy_dokumentov_o_kommercheskom_uchete_elektricheskoj_energii') {
    $("#tipovye_formy_dokumentov_o_kommercheskom_uchete_elektricheskoj_energii").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/kommercheskij_uchet_elektricheskoj_energii/trebovaniya_k_organizacii_ucheta') {
    $("#trebovaniya_k_organizacii_ucheta").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/ofisy_obsluzhivaniya_potrebitelej' ||
    window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi' ||
    window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/interaktivnaya_obratnaya_svyaz' ||
    window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej' ||
    window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/lichnyj_kabinet_potrebitelya' ||
    window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/voprosy_i_otvety') {
    $("#obsluzhivanie_potrebitelej_vision ul").addClass('sidebar-dropdown list-unstyled collapse show');
    $("#obsluzhivanie_potrebitelej_vision a").addClass('sidebar-link');
    $("#obsluzhivanie_potrebitelej_vision a").attr("aria-expanded", "true");
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/ofisy_obsluzhivaniya_potrebitelej') {
    $("#ofisy_obsluzhivaniya_potrebitelej").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi') {
    $("#zaochnoe_obsluzhivanie_posredstvom_telefonnoj_svyazi").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/interaktivnaya_obratnaya_svyaz') {
    $("#interaktivnaya_obratnaya_svyaz").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej') {
    $("#normativnye_dokumenty_po_obsluzhivaniyu_potrebitelej").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/lichnyj_kabinet_potrebitelya') {
    $("#lichnyj_kabinet_potrebitelya").addClass('sidebar-item active');
}
;

if (window.location.pathname === '/potrebitelyam/obsluzhivanie_potrebitelej/voprosy_i_otvety') {
    $("#voprosy_i_otvety").addClass('sidebar-item active');
}
;