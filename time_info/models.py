from django.db import models
from club.models import Club

# Create your models here.
class TimeInfo(models.Model):
    time_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club = models.ForeignKey(Club, to_field='club_id', on_delete=models.CASCADE)

    time_info = models.TimeField()

    class Meta:
        managed = False
        db_table = 'time_info'
