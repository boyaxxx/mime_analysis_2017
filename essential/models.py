from django.db import models


# Create your models here.
class TotalStatistics(models.Model):
    register_count = models.IntegerField(default=0)
    login_count = models.IntegerField(default=0)


class DailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    register_count = models.IntegerField(default=0)
    login_count = models.IntegerField(default=0)

