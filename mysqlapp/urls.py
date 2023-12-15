"""
URL configuration for mysqlapp app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('info', views.InfoView.as_view(), name='info'),

    path('personas_info', views.pInfoView.as_view(), name='personas_info'),
    path('partners_info', views.paInfoView.as_view(), name='partners_info'),
    path('workers_info', views.wInfoView.as_view(), name='workers_info'),
    path('clients_info', views.clInfoView.as_view(), name='clients_info'),
    path('contracts_info', views.coInfoView.as_view(), name='contracts_info'),

    path('person_create', views.pCreateView.as_view()),
    path('partner_create', views.paCreateView.as_view()),
    path('worker_create', views.wCreateView.as_view()),
    path('client_create', views.clCreateView.as_view()),
    path('contract_create', views.coCreateView.as_view()),

    path('person_update/<pk>', views.pUpdateView.as_view()),
    path('partner_update/<pk>', views.paUpdateView.as_view()),
    path('worker_update/<pk>', views.wUpdateView.as_view()),
    path('client_update/<pk>', views.clUpdateView.as_view()),
    path('contract_update/<pk>', views.coUpdateView.as_view()),

    path('person_delete/<pk>', views.pDeleteView.as_view()),
    path('partner_delete/<pk>', views.paDeleteView.as_view()),
    path('worker_delete/<pk>', views.wDeleteView.as_view()),
    path('client_delete/<pk>', views.clDeleteView.as_view()),
    path('contract_delete/<pk>', views.coDeleteView.as_view()),
]
