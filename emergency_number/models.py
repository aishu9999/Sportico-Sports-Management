from django.db import models

# Create your models here.
class EmergencyNumber(models.Model):
    em_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    service = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'emergency_number'

