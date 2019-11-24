from django.db import models


class UsdJpy(models.Model):
    time_stamp = models.CharField(max_length=128)
    usd_jpy = models.CharField(max_length=128)

    def __str__(self):
        return self.time_stamp
