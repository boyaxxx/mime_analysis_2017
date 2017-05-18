from django.db import models


# Create your models here.
class Doctor(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    age = models.CharField()
    province = models.CharField()
    city = models.CharField()
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
    login_year = models.IntegerField()
    login_month = models.IntegerField()
    login_day = models.IntegerField()


