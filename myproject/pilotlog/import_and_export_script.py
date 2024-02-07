
import csv
import json
from models import SettingConfig

def format_json_file(file_path):
    print("Opening the JSON file...")
    with open(file_path, 'r', encoding='utf-8') as file:
        json_string = file.read()

    print("JSON file read successfully.")

    print("Removing escape backslashes...")
    json_string = json_string.replace("\\", "")

    print("Loading the JSON string into a Python object...")
    data = json.loads(json_string)

    print("Writing the Python object back to the file as formatted JSON...")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("JSON file formatted successfully.")

    return data

# Assuming the file path is 'Data/import - pilotlog_mcc.json'
print("Formatting the JSON file...")
data = format_json_file('Data/import - pilotlog_mcc.json')

print("Creating SettingConfig objects from the data...")
setting_configs = [SettingConfig.from_dict(item) for item in data]

print("SettingConfig objects created successfully.")

# Print the result
print("Result:")
print(json.dumps(data, indent=4))


def export_data_to_csv(data, file_path):
    print("Exporting data to CSV...")

    # Define the column names based on the attributes of the SettingConfig class
    fieldnames = ['user_id', 'table', 'guid', 'meta', 'platform', '_modified']

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in data:
            # Convert the SettingConfig object to a dictionary
            row = {
                'user_id': obj.user_id,
                'table': obj.table,
                'guid': obj.guid,
                'meta': obj.meta,
                'platform': obj.platform,
                '_modified': obj._modified
            }
            writer.writerow(row)

    print("Data exported to CSV successfully.")

# Export the data to a CSV file
export_data_to_csv(setting_configs, 'Data/export.csv')

