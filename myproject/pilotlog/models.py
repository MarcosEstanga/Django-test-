from django.db import models

class SettingConfigQuerySet(models.QuerySet):
    def with_meta_info(self):
        """Filters setting configurations that have metadata information."""
        return self.exclude(meta={})

class SettingConfig(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=100)
    guid = models.UUIDField()
    meta = models.JSONField()
    platform = models.CharField(max_length=100)
    modified = models.DateTimeField(auto_now=True)

     objects = models.Manager.from_queryset(SettingConfigQuerySet)()

    def __str__(self):
        return f"{self.user_id} - {self.table}"

    class Meta:
        ordering = ['user_id']  # Optional: Ordering of records when queried
