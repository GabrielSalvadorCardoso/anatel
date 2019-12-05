from django.contrib.gis.db import models
from hyper_resource.models import FeatureModel

class Estacao(FeatureModel):
    gid = models.AutoField(primary_key=True)
    #id_plano_b = models.IntegerField(blank=True, null=True)
    numfistel = models.CharField(max_length=254, blank=True, null=True)
    nomefase = models.CharField(max_length=254, blank=True, null=True)
    siglauf = models.CharField(max_length=254, blank=True, null=True)
    nomemunici = models.CharField(max_length=254, blank=True, null=True)
    nomeentida = models.CharField(max_length=254, blank=True, null=True)
    numservico = models.CharField(max_length=254, blank=True, null=True)
    servico = models.CharField(max_length=254, blank=True, null=True)
    codcanal = models.CharField(max_length=254, blank=True, null=True)
    #medlatitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #medlongitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #mederpmax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    classe = models.CharField(max_length=254, blank=True, null=True)
    metadado = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacao'

