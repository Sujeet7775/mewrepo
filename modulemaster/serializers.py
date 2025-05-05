from rest_framework import serializers
from .models import ModuleMaster

class ModuleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleMaster
        fields = '__all__'


