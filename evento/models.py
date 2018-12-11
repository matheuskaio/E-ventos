from django.db import models
from promotor.models import PromotorEventos

# Create your models here.

class Ingresso():
    pass
class Evento(models.Model):
    promotores = models.ManyToManyField(PromotorEventos, null=False, blank=False)
    nomeDaAtracao = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(null=False, blank=False)
    foto = models.ImageField(upload_to='eventos_photos', null=True, blank=True)
    cidade = models.CharField(max_length=50, blank=False)
    rua = models.CharField(max_length=30, blank=False)
    bairro = models.CharField(max_length=20, blank=False)
    numero = models.CharField(max_length=5, blank=False)
    estado = models.CharField(max_length=2, blank=False)
    complemento = models.CharField(max_length=50, blank=False)
    quantidaIngresso = models.CharField(max_length=4)