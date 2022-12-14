# Generated by Django 4.0.5 on 2022-07-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgnt', '0008_alter_invoice_quantity_check_alter_invoice_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_P_U',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='item_price'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_P_V_HTVA',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='item_price_nvat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_P_V_TVAC',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='item_price_wvat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_T_V_A',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='vat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_chequier',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='item_quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_P_U',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='item_price'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_P_V_HTVA',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='item_price_nvat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_P_V_TVAC',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='item_price_wvat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_T_V_A',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='vat'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_chequier',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='item_quantity'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_HTVA',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='Total HTVA:'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_TVA',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='Total TVA:'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_TVAC',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7, null=True, verbose_name='Total TVAC:'),
        ),
    ]
