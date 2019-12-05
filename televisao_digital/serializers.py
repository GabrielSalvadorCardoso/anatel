from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class EstacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Estacao
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = [
            'gid',
            #'id_plano_b',
            'numfistel',
            'nomefase',
            'siglauf',
            'nomemunici',
            'nomeentida',
            'numservico',
            'servico',
            'codcanal',
            #'medlatitud',
            #'medlongitu',
            #'mederpmax',
            'classe',
            'metadado'
        ]
