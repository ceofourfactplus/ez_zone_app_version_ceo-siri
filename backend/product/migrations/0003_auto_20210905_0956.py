# Generated by Django 3.2.6 on 2021-09-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_categort_productcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='status',
            field=models.IntegerField(choices=[('1', 'true'), ('0', 'false')], default='1'),
        ),
        migrations.AddField(
            model_name='salechannel',
            name='status',
            field=models.IntegerField(choices=[('1', 'able'), ('0', 'disable')], default='1'),
        ),
    ]
