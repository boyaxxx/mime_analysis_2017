from django.db import models


# Create your models here.
class TotalStatistics(models.Model):
    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)

    order_count = models.IntegerField(default=0)
    turnover_count = models.IntegerField(default=0)
    live_count = models.IntegerField(default=0)
    group_count = models.IntegerField(default=0)


class RegionStatistics(models.Model):
    province = models.CharField()
    city = models.CharField()
    longitude = models.DecimalField(12, 6)
    latitude = models.DecimalField(12, 6)

    register_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)
    turnover_count = models.IntegerField(default=0)
    live_count = models.IntegerField(default=0)
    group_count = models.IntegerField(default=0)


class DailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)
    login_count = models.IntegerField(default=0)

    order_count = models.IntegerField(default=0)
    turnover_count = models.IntegerField(default=0)

    live_count = models.IntegerField(default=0)
    group_count = models.IntegerField(default=0)

