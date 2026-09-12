from django.db import models
from club.models import Club

# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club=models.ForeignKey(Club,to_field='club_id',on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'location'
