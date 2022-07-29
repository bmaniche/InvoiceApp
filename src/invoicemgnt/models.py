from django.db import models

# Create your models here.
class Invoice(models.Model):
	comments = models.TextField(max_length=3000, default='', blank=True, null=True)
	invoice_number = models.IntegerField(blank=True, null=True)
	invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	name = models.CharField('Customer Name', max_length=300, default='', blank=True, null=True)
	
	
	line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
	line_one_chequier = models.IntegerField('item_quantity', default='', blank=True, null=True)
	line_one_P_U = models.IntegerField('item_price', default='', blank=True, null=True)
	line_one_P_V_HTVA = models.IntegerField('item_price_nvat', default='', blank=True, null=True)
	line_one_T_V_A = models.IntegerField('vat', default='', blank=True, null=True)
	line_one_P_V_TVAC= models.IntegerField('item_price_wvat', default='', blank=True, null=True)

	line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
	line_two_chequier = models.IntegerField('item_quantity', default='', blank=True, null=True)
	line_two_P_U = models.IntegerField('item_price', default='', blank=True, null=True)
	line_two_P_V_HTVA = models.IntegerField('item_price_nvat', default='', blank=True, null=True)
	line_two_T_V_A = models.IntegerField('vat', default='', blank=True, null=True)
	line_two_P_V_TVAC= models.IntegerField('item_price_wvat', default='', blank=True, null=True)

	

	p_o_box = models.CharField('P.O.Box: ',max_length=120, default='', blank=True, null=True)
	total_HTVA = models.IntegerField('Total HTVA:',default='', blank=True, null=True)
	total_TVA = models.IntegerField('Total TVA:',default='', blank=True, null=True)
	total_TVAC = models.IntegerField('Total TVAC:',default='', blank=True, null=True)
	Quantity_check = models.IntegerField('Nombre de chéquiers:',default='', blank=True, null=True)
	balance = models.IntegerField(default='', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
	paid = models.BooleanField(default=False)
	invoice_type_choice = (
			
			('Facture', 'Facture'),
		)
	invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

	def __str__(self):
		return self.name + '-' + str(self.invoice_number)