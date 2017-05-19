from django.db import models


# Create your models here.
class AgeRange(models.Model):
    range = models.CharField()
    range_description = models.CharField()


class HospitalLevel(models.Model):
    level = models.CharField()
    level_description = models.CharField()


class HospitalOffice(models.Model):
    office = models.CharField()
    office_description = models.CharField()


class DoctorTitle(models.Model):
    title = models.CharField()
    title_description = models.CharField()


class Doctor(models.Model):
    name = models.CharField()
    real_name = models.CharField(null=True)
    phone = models.CharField(max_length=11, unique=True)
    age_range = models.ForeignKey(AgeRange)
    doctor_title = models.ForeignKey(DoctorTitle)
    hospital_level = models.ForeignKey(HospitalLevel)
    hospital_office = models.ForeignKey(HospitalOffice)
    province = models.CharField()
    city = models.CharField()
    longitude = models.DecimalField(12, 6)
    latitude = models.DecimalField(12, 6)
    register_year = models.CharField()
    register_month = models.CharField()
    register_day = models.CharField()
    register_time = models.DateTimeField()


class AgeRangeTotalStatistics(models.Model):
    age_range = models.ForeignKey(AgeRange)
    count = models.IntegerField(default=0)


class AgeRangeDailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    age_range = models.ForeignKey(AgeRange)
    count = models.IntegerField(default=0)


class HospitalLevelTotalStatistics(models.Model):
    hospital_level = models.ForeignKey(HospitalLevel)
    count = models.IntegerField(default=0)


class HospitalLevelDailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    hospital_level = models.ForeignKey(HospitalLevel)
    count = models.IntegerField(default=0)


class HospitalOfficeTotalStatistics(models.Model):
    hospital_office = models.ForeignKey(HospitalOffice)
    count = models.IntegerField(default=0)


class HospitalOfficeDailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    hospital_office = models.ForeignKey(HospitalOffice)
    count = models.IntegerField(default=0)


class DoctorTitleTotalStatistics(models.Model):
    doctor_title = models.ForeignKey(DoctorTitle)
    count = models.IntegerField(default=0)


class DoctorTitleDailyStatistics(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    doctor_title = models.ForeignKey(DoctorTitle)
    count = models.IntegerField(default=0)
