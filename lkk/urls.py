# lkk/urls.py
from django.urls import path
from .views import zayavka_new,\
    profile_view, profile_edit, profile_del, profile_adres, profile_adres_edit, profile_adres_del,\
    zayavitel, zayavitel_edit, zayavitel_del,\
    main_lk, zayavka_view, zayavka_del, zayavka_send, zayavka_create, zayavka_detail, register,\
    epu_edit, epu_del, epu_view, git_update
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
    path('profile_epu/<int:pkk>/', epu_view, name='epu'),
    path('profile_epu/edit/<int:pkk>/', epu_edit, name='zayavitel_edit'),
    path('profile_epu/delete/<int:pkk>/', epu_del, name='zayavitel_del'),
    path('cajryrtkrybktktukjvrbjykkturvjecevjtuktiyllkrreqwwgeqh5thrtjrw/', git_update, name='git_update'),
    path('', main_lk, name='main_lk'),

]