from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['name', 'invoice_number','p_o_box', 'invoice_date']
   form = InvoiceForm
   list_filter = ['name','invoice_number']
   search_fields = ['name', 'invoice_number']

admin.site.register(Invoice, InvoiceAdmin)



