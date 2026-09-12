from django.db import models
from club.models import Club
from time_info.models import TimeInfo

# Create your models here.
class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club=models.ForeignKey(Club,to_field='club_id',on_delete=models.CASCADE)
    services = models.CharField(max_length=50)
    time = models.CharField(max_length=30)
    equipments = models.CharField(max_length=50)
    games = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facilities'
