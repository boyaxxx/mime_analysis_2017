from django.db import models


# Create your models here.
class AgeRange(models.Model):
    range = models.CharField()
    range_description = models.CharField()


class Doctor(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    province = models.CharField()
    city = models.CharField()
    age_range = models.ForeignKey(AgeRange)
    hospital_level = models.CharField()
    hospital_office = models.CharField()


class RegisterStatistics(models.Model):
    doctor = models.ForeignKey(Doctor)
    register_year = models.IntegerField()
    register_month = models.IntegerField()
    register_day = models.IntegerField()


class LoginStatistics(models.Model):
    doctor = models.ForeignKey(Doctor)
    login_year = models.IntegerField()
    login_month = models.IntegerField()
    login_day = models.IntegerField()


class AuthorizeStatistics(models.Model):
    doctor = models.ForeignKey(Doctor)
    authorize_year = models.IntegerField()
    authorize_month = models.IntegerField()
    authorize_day = models.IntegerField()

