from django import forms
from .models import Invoice

required = 'This field is required'

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'p_o_box', 'invoice_date','invoice_number',
				'line_one', 'line_one_chequier', 'line_one_P_U', 'line_one_P_V_HTVA','line_one_T_V_A','line_one_P_V_TVAC',
				'line_two', 'line_two_chequier', 'line_two_P_U', 'line_two_P_V_HTVA','line_two_T_V_A','line_two_P_V_TVAC',
				 
				'total_HTVA', 'total_TVA', 'total_TVAC', 'paid', 'invoice_type','Quantity_check'
				]
	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError(required)
		return invoice_number


	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError(required)
		return name


	def clean_line_one(self):
		line_one = self.cleaned_data.get('line_one')
		if not line_one:
			raise forms.ValidationError(required)
		return line_one

	def clean_line_one_chequier(self):
		line_one_chequier = self.cleaned_data.get('line_one_chequier')
		if not line_one_chequier:
			raise forms.ValidationError(required)
		return line_one_chequier

class InvoiceSearchForm(forms.ModelForm):
	generate_invoice = forms.BooleanField(required=False)
	class Meta:
		model = Invoice
		fields = ['invoice_number', 'name','generate_invoice']



class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'p_o_box', 'invoice_date','invoice_number',
				'line_one', 'line_one_chequier', 'line_one_P_U', 'line_one_P_V_HTVA','line_one_T_V_A','line_one_P_V_TVAC',
				'line_two', 'line_two_chequier', 'line_two_P_U', 'line_two_P_V_HTVA','line_two_T_V_A','line_two_P_V_TVAC',
				 
				'total_HTVA', 'total_TVA', 'total_TVAC', 'paid', 'invoice_type','Quantity_check'
				]
	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError(required)
		return invoice_number


	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError(required)
		return name


	def clean_line_one(self):
		line_one = self.cleaned_data.get('line_one')
		if not line_one:
			raise forms.ValidationError(required)
		return line_one

	def clean_line_one_chequier(self):
		line_one_chequier = self.cleaned_data.get('line_one_chequier')
		if not line_one_chequier:
			raise forms.ValidationError(required)
		return line_one_chequier