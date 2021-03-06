# Generated by Django 3.2.6 on 2021-09-25 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.IntegerField()),
                ('payment', models.CharField(choices=[('cash', 'จ่ายสด'), ('transfer', 'โอน')], max_length=8)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_create_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('female', 'ผู้หญิง'), ('male', 'ผู้ชาย')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
                ('minstock', models.IntegerField()),
                ('avg_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('cateogry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.category')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_create_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('descriptions', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockTrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_trance_create_by', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='max_price_supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stock_max_price_supplier', to='stock.supplier'),
        ),
        migrations.AddField(
            model_name='stock',
            name='min_price_supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stock_min_price_supplier', to='stock.supplier'),
        ),
        migrations.AddField(
            model_name='stock',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.unit'),
        ),
        migrations.AddField(
            model_name='stock',
            name='update_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OrderToBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.IntegerField()),
                ('remark', models.TextField(blank=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_detail_create_by', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.invoice')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.stock')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.supplier')),
                ('update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_detail_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.payer'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.supplier'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='update_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_update_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
