from django.db import models
from club.models import Club

# Create your models here.
class LocateClub(models.Model):
    locate_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club=models.ForeignKey(Club,to_field='club_id',on_delete=models.CASCADE)
    location = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'locate_club'
