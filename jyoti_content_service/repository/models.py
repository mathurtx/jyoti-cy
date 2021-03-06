from django.db import models

class ReportTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    report_type = models.CharField(max_length=30)
    report_content = models.CharField(max_length=300)
    evidence = models.CharField(max_length=100, blank=True)
    data_source = models.CharField(max_length=2)
    city = models.CharField(max_length=50, blank=True)

class LocationFactTable(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    report_type = models.CharField(max_length=30)
    report_type_count = models.IntegerField(default=0)

class ReportCountFactTable(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    report_count = models.ImageField(default=0)



