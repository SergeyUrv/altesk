# lkk/urls.py
from django.urls import path
# from .views import zayavka_new,\
#     profile_view, profile_edit, profile_del, profile_adres, profile_adres_edit, profile_adres_del,\
#     zayavitel, zayavitel_edit, zayavitel_del,\
#     main_lk, zayavka_view, zayavka_view_admin, zayavka_del, zayavka_send, zayavka_create, zayavka_detail, register,\
#     epu_edit, epu_del, epu_view, obracheniya_view, obracheniya_edit
from .views import *
from django.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='signup'),
    path('zayavka/', zayavka_view, name='zayavki'),
    path('zayavka/edit/<int:pkk>/', zayavka_new, name='new_zayavka'),
    path('zayavka/delete/<int:pkk>/', zayavka_del, name='zayavka_del'),
    path('zayavka/send/<int:pkk>/', zayavka_send, name='zayavka_send'),
    path('zayavka/create/<int:pkk>/', zayavka_create, name='zayavka_create'),
    path('zayavka/detail/<int:pkk>/', zayavka_detail, name='zayavka_detail'),
    path('profile_fio/', profile_view, name='person'),
    path('profile_fio/edit/<int:pkk>/', profile_edit, name='person_edit'),
    path('profile_fio/delete/<int:pkk>/', profile_del, name='person_del'),
    path('profile_adres/', profile_adres, name='adres'),
    path('profile_adres/edit/<int:pkk>/', profile_adres_edit, name='adres_edit'),
    path('profile_adres/delete/<int:pkk>/', profile_adres_del, name='adres_del'),
    path('profile_zayavitel/', zayavitel, name='zayavitel'),
    path('profile_zayavitel/edit/<int:pkk>/', zayavitel_edit, name='zayavitel_edit'),
    path('profile_zayavitel/delete/<int:pkk>/', zayavitel_del, name='zayavitel_del'),
    path('profile_epu/', epu_view, name='epu'),
    path('profile_epu/edit/<int:pkk>/', epu_edit, name='epu_edit'),
    path('profile_epu/delete/<int:pkk>/', epu_del, name='epu_del'),
    path('obracheniya/', obracheniya_view, name='obracheniya'),
    path('obracheniya/edit/<int:pkk>/', obracheniya_edit, name='obracheniya_edit'),
    path('zayavki/', zayavka_view_admin, name='zayavki_admin'),
    path('zayavka_status_vrab/<int:pkk>/', zayavka_status_vrab, name='zayavka_status_vrab'),
    path('zayavka_status_edit/<int:pkk>/', zayavka_status_edit, name='zayavka_status_edit'),
    path('zayavka_status_obr/<int:pkk>/', zayavka_status_obr, name='zayavka_status_obr'),
    path('zayavka_status_obreso/<int:pkk>/', zayavka_status_obreso, name='zayavka_status_obreso'),
    path('zayavka_status_canc/<int:pkk>/', zayavka_status_canc, name='zayavka_status_canc'),
    path('zayavka_status_doc/<int:pkk>/', zayavka_status_doc, name='zayavka_status_doc'),
    path('zayavka_status_wpod/<int:pkk>/', zayavka_status_wpod, name='zayavka_status_wpod'),
    path('zayavka_status_done/<int:pkk>/', zayavka_status_done, name='zayavka_status_done'),

#    path('obracheniya/delete/<int:pkk>/', obracheniya_del, name='obracheniya_del'),
    path('', main_lk, name='main_lk'),

]