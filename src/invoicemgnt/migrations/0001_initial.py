# Generated by Django 4.0.5 on 2022-06-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, default='', max_length=3000, null=True)),
                ('invoice_number', models.IntegerField(blank=True, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Customer Acronyme')),
                ('full_name', models.CharField(blank=True, default='', max_length=3000, null=True, verbose_name='Customer Name')),
                ('line_one', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 1')),
                ('line_one_chequier', models.IntegerField(blank=True, default=0, null=True, verbose_name='chéquiers')),
                ('line_one_P_U', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.U.')),
                ('line_one_P_V_HTVA', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.V. HTVA')),
                ('line_one_T_V_A', models.IntegerField(blank=True, default=0, null=True, verbose_name='T.V.A')),
                ('line_one_P_V_TVAC', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.V. TVAC')),
                ('line_two', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 2')),
                ('line_two_chequier', models.IntegerField(blank=True, default=0, null=True, verbose_name='chéquiers')),
                ('line_two_P_U', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.U.')),
                ('line_two_P_V_HTVA', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.V. HTVA')),
                ('line_two_T_V_A', models.IntegerField(blank=True, default=0, null=True, verbose_name='T.V.A')),
                ('line_two_P_V_TVAC', models.IntegerField(blank=True, default=0, null=True, verbose_name='P.V. TVAC')),
                ('phone_number', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('total', models.IntegerField(blank=True, default='0', null=True)),
                ('balance', models.IntegerField(blank=True, default='0', null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('invoice_type', models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Proforma Invoice', 'Proforma Invoice'), ('Invoice', 'Invoice')], default='', max_length=50, null=True)),
            ],
        ),
    ]
