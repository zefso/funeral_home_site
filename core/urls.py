from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('precaution/', views.precaution, name='precaution'),
    path('funeral_speeches/', views.funeral_speeches, name='funeral_speeches'),
    path('farewell/', views.farewell, name='farewell'),
    path('contact/', views.contact, name='contact'),
    path('i18n/', include('django.conf.urls.i18n')),
]
