# lkk/urls.py
from django.urls import path
from .views import SignUpView, zayavka_new, profile_ur, profile, profile_view, profile_edit
from django.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('zayavka/new/', zayavka_new, name='new_zayavka'),
    path('profile/<int:step>/', profile, name='profile'),
    path('profile_fio/', profile_view, name='person'),
    path('profile_fio/edit/<int:pkk>/', profile_edit, name='person_edit'),

]