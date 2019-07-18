from rest_framework import serializers
from .models import Store
from .models import Place
from .models import Test

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

        fields=('id', 'GPSX', 'GPSY', 'LARG_CATE', 'MID_CATE', 'SMALL_CATE', 'NAME', 'IMAGENAME', 'IMAGE');
