from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import SettingConfig

class SettingConfigSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SettingConfig
        fields = ['user_id', 'table', 'guid', 'meta', 'platform', 'modified']

