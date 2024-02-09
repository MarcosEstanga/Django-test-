from rest_framework import serializers
from .models import SettingConfig

class SettingConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingConfig
        fields = ['user_id', 'table', 'guid', 'meta', 'platform', 'modified']
