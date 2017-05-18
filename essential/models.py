from django.db import models


# Create your models here.
class TotalStatistics(models.Model):
    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    login_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)


class DailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    visit_count = models.IntegerField(default=0)
    register_count = models.IntegerField(default=0)
    login_count = models.IntegerField(default=0)
    authorize_count = models.IntegerField(default=0)

