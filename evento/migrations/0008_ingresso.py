# Generated by Django 2.1.4 on 2019-01-04 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20190104_1101'),
        ('promotor', '0001_initial'),
        ('evento', '0007_auto_20181227_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDaAtracao', models.CharField(max_length=50)),
                ('pk_aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientes.Aluno')),
                ('promotores', models.ManyToManyField(blank=True, null=True, to='promotor.PromotorEventos')),
            ],
        ),
    ]