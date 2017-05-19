from django.db import models


# Create your models here.
class DailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)

    order_count = models.IntegerField(default=0)
    turnover_count = models.IntegerField(default=0)


class DailyRegionStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    province = models.CharField()
    longitude = models.DecimalField(12, 6)
    latitude = models.DecimalField(12, 6)

    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)

    order_count = models.IntegerField(default=0)
    turnover_count = models.IntegerField(default=0)
