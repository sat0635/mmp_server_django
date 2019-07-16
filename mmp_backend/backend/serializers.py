from rest_framework import serializers
from .models import Store
from .models import Place


class NearStoreSerializer(serializers.HyperlinkedModelSerializer):
    IMAGE = serializers.ImageField(use_url=True)
    class Meta:
        fields = (
            'id',
            'GPSX',
            'GPSY',
            'LARG_CATE',
            'MID_CATE',
            'SMALL_CATE',
            'NAME',
            'IMAGENAME',
            'IMAGE',
        )
        model = Store
