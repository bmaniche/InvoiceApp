from rest_framework import serializers
from invoicemgnt.models import Invoice



class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['name', 'p_o_box', 'invoice_date','invoice_number',
                'line_one', 'line_one_chequier', 'line_one_P_U', 'line_one_P_V_HTVA','line_one_T_V_A','line_one_P_V_TVAC',
                'line_two', 'line_two_chequier', 'line_two_P_U', 'line_two_P_V_HTVA','line_two_T_V_A','line_two_P_V_TVAC',
                 
                'total_HTVA', 'total_TVA', 'total_TVAC', 'paid', 'invoice_type','Quantity_check'
                ]