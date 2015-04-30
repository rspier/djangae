from django.db import models

from djangae import patches


class CounterShard(models.Model):
    count = models.PositiveIntegerField()

    class Meta:
        app_label = "djangae"

# Apply our django patches
patches.patch()
