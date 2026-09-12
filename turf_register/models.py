from django.db import models

# Create your models here.
class TurfRegister(models.Model):
    turf_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contactno = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    lat = models.CharField(max_length=30)
    lon = models.CharField(max_length=30)


    class Meta:
        managed = False
        db_table = 'turf_register'

