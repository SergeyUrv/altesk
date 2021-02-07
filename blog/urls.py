from django.urls import path
from . import views

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.main_zagl, name='main_zagl'),
    path('ru/raskritie_informacii/', views.main_raskritie, name='raskritie'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path("genres/", views.show_genres),
]