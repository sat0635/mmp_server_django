from rest_framework import serializers
from .models import Store
from .models import Place
from .models import Test

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test

        fields=('id', 'version',)
