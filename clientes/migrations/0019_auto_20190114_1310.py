# Generated by Django 2.1.4 on 2019-01-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_auto_20190106_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=969301, max_length=14, null=True),
        ),
    ]
