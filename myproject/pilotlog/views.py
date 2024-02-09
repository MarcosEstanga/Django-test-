from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import SettingConfig
from .serializers import SettingConfigSerializer
import csv
import json

@api_view(['GET'])
def format_and_export_data(request):
    # Format the JSON file
    with open('Data/import - pilotlog_mcc.json', 'r', encoding='utf-8') as file:
        json_string = file.read().replace("\\", "")
    data = json.loads(json_string)

    # Create SettingConfig objects from the data
    setting_configs = [SettingConfig(**item) for item in data]
    SettingConfig.objects.bulk_create(setting_configs)

    # Serialize the data
    serializer = SettingConfigSerializer(setting_configs, many=True)
    serialized_data = serializer.data

    # Write the serialized data to a CSV file
    with open('Data/export.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['user_id', 'table', 'guid', 'meta', 'platform', 'modified']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for obj in serialized_data:
            writer.writerow({
                'user_id': obj['user_id'],
                'table': obj['table'],
                'guid': obj['guid'],
                'meta': json.dumps(obj['meta']),
                'platform': obj['platform'],
                'modified': obj['modified']
            })

    # Return the serialized data as a JSON response
    return JsonResponse(serialized_data, safe=False)
