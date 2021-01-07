# lkk/urls.py
from django.urls import path
from .views import SignUpView
from django.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]