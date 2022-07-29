from django.urls import url
from invoicemgnt import views

url(r'^invoices/$', views.list_invoice,),