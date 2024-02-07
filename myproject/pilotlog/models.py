from django.db import models

# models.py

class SettingConfig:
    def __init__(self, user_id, table, guid, meta, platform, _modified):
        self.user_id = user_id
        self.table = table
        self.guid = guid
        self.meta = meta
        self.platform = platform
        self._modified = _modified

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            user_id=data_dict.get('user_id'),
            table=data_dict.get('table'),
            guid=data_dict.get('guid'),
            meta=data_dict.get('meta'),
            platform=data_dict.get('platform'),
            _modified=data_dict.get('_modified')
        )

# Now you have a list of SettingConfig objects stored in 'setting_configs'