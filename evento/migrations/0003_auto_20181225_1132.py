# Generated by Django 2.1.4 on 2018-12-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20181225_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/eventos_photos'),
        ),
    ]
