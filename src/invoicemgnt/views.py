from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required


# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab


# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "base.html",context)

@login_required
def add_invoice(request):
	form = InvoiceForm(request.POST or None)
	total_invoices = Invoice.objects.count()
	queryset = Invoice.objects.order_by('invoice_date')[:6]
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		
	context = {
		"form": form,
		"title": "New Invoice",
		"total_invoices": total_invoices,
		"queryset": queryset,
	}
	return render(request, "entry.html", context)
	
@login_required 
def list_invoice(request):

	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}
	


	if request.method == 'POST':
		queryset = Invoice.objects.filter(
									invoice_number__icontains=form['invoice_number'].value(),
									name__icontains=form['name'].value()
									)
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}

	if form['generate_invoice'].value() == True:
			instance = queryset
			data_file = instance
			num_of_invoices = len(queryset)
			message = str(num_of_invoices) + " invoices successfully generated."
			messages.success(request, message)
			#return redirect('/getpdf')
			

			def import_data(data_file):
				
				invoice_data = data_file
				for row in invoice_data:
					invoice_type = row.invoice_type
					invoice_number = row.invoice_number
					invoice_date = row.invoice_date
				name = row.name
				
				p_o_box = row.p_o_box

				line_one = row.line_one
				line_one_chequier = row.line_one_chequier
				line_one_P_U  = row.line_one_P_U 
				line_one_P_V_HTVA = row.line_one_P_V_HTVA
				line_one_T_V_A = row.line_one_T_V_A
				line_one_P_V_TVAC = row.line_one_P_V_TVAC

				line_two = row.line_two
				line_two_chequier = row.line_two_chequier
				line_two_P_U = row.line_two_P_U
				line_two_P_V_HTVA = row.line_two_P_V_HTVA
				line_two_T_V_A = row.line_two_T_V_A
				line_two_P_V_TVAC = row.line_two_P_V_TVAC

				total_HTVA = row.total_HTVA
				total_TVA = row.total_TVA
				total_TVAC = row.total_TVAC
				Quantity_check = row.Quantity_check

				pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
			

				generate_invoice(str(name), str(invoice_number), 
					str(line_one), str(line_one_chequier), str(line_one_P_U ), 
					str(line_one_P_V_HTVA),str(line_one_T_V_A),str(line_one_P_V_TVAC), str(line_two), str(line_two_chequier),
					str(line_two_P_U), str(line_two_P_V_HTVA),str(line_two_T_V_A),str(line_two_P_V_TVAC),str(total_HTVA),
					str(total_TVA),str(total_TVAC),str(Quantity_check), str(p_o_box), str(invoice_date),
					str(invoice_type), pdf_file_name)

			def generate_invoice(name, invoice_number, 
					line_one, line_one_chequier, line_one_P_U , line_one_P_V_HTVA, line_one_T_V_A, line_one_P_V_TVAC,
					line_two, line_two_chequier, line_two_P_U, line_two_P_V_HTVA, line_two_T_V_A, line_two_P_V_TVAC, 
					total_HTVA, total_TVA, total_TVAC, Quantity_check, p_o_box, invoice_date, invoice_type, pdf_file_name):
				

				c = canvas.Canvas(pdf_file_name)

			# image of seal
				logo = 'NSI_logo-.jpg'
				c.drawImage(logo, 50, 700, width=500, height=120)

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(400, 660, str(invoice_type) + ':')
			
				invoice_number_string = str('00' + invoice_number)
				c.drawCentredString(490, 660, invoice_number_string)


			
				c.drawCentredString(409, 640, "Date:")
				c.drawCentredString(492, 641, invoice_date)


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(397, 600, "centre fiscal : ")
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(484, 602, 'DGC')

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(397, 580, "secteur d'activité : ")
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(484, 583, 'services')

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(397, 560, "forme juridique : ")
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(484, 564, 's.a.r.l')


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(80, 660, "client:")
				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(150, 660, name)

				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(80, 640, full_name)

				
				c.drawCentredString(90, 620, p_o_box)     

				c.setFont('Helvetica-Bold', 14, leading=None)
				c.drawCentredString(310, 580, str(invoice_type))
				c.drawCentredString(310, 560, "Carnet de check"+invoice_date)
				c.drawCentredString(295, 510, "__________________________________________________________")
				

				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(110, 520, 'Désignation')     
				c.drawCentredString(220, 520, 'item_quantity')     
				c.drawCentredString(330, 520, 'item_price')     
				c.drawCentredString(440, 520, 'item_price_nvat')
				c.drawCentredString(550, 520, 'vat')
				c.drawCentredString(650, 520, 'item_price_wvat')  


				c.setFont('Helvetica', 12, leading=None)
				c.drawCentredString(110, 490, line_one)     
				c.drawCentredString(220, 490, line_one_chequier)     
				c.drawCentredString(330, 490, line_one_P_U )     
				c.drawCentredString(440, 490, line_one_P_V_HTVA)
				c.drawCentredString(550, 490, line_one_T_V_A)
				c.drawCentredString(650, 490, line_one_P_V_TVAC)    

				if line_two != '':
					c.setFont('Helvetica', 12, leading=None)
					c.drawCentredString(110, 460, line_two)     
					c.drawCentredString(220, 460, line_two_chequier)     
					c.drawCentredString(330, 460, line_two_P_U)     
					c.drawCentredString(450, 460, line_two_P_V_HTVA)     
					c.drawCentredString(550, 460, line_two_T_V_A)
					c.drawCentredString(650, 460, line_two_P_V_TVAC)
				    

				# TOTAL
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(120, 140, 'Nombre de chéquiers:')
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(290, 140, Quantity_check)
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(400, 140, 'Total HTVA:')
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(484, 140, total_HTVA) 
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(400, 120, 'Total TVA:')
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(484, 120, total_TVA)
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(400, 100, 'Total TVAC:')
				c.setFont('Helvetica-Bold', 20, leading=None)
				c.drawCentredString(484, 100, total_TVAC)

				# SIGN
				c.setFont('Helvetica-Bold', 12, leading=None)
				c.drawCentredString(150, 90, "Signed:__________________")
				


				c.showPage()
				c.save()
				

				import_data(data_file)

	
			

	return render(request, "list_invoice.html", context)



	

	
@login_required
def update_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	form = InvoiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InvoiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_invoice')

	context = {
		'form':form
	}
	return render(request, 'entry.html', context)

def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_invoice')
	return render(request, 'delete_invoice.html')