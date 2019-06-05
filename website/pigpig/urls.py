from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'pigpig'
urlpatterns = [
    path('', views.pigpig, name='pigpig'),
    path('index-cut/', views.indexCut, name='indexCut'),
    path('a/', views.aa, name='a'),
    path('b/', views.bb, name='b'),
    path('c/', views.cc, name='c'),
    path('d/', views.dd, name='d'),
    path('e/', views.ee, name='e'),
    path('f/', views.ff, name='f'),
    path('g/', views.gg, name='g'),
    path('h/', views.hh, name='h'),
    path('i/', views.ii, name='i'),
    path('j/', views.jj, name='j'),
    path('k/', views.kk, name='k'),

]