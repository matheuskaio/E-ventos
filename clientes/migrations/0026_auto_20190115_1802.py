# Generated by Django 2.1.4 on 2019-01-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0025_auto_20190115_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=248263, max_length=14, null=True),
        ),
    ]
