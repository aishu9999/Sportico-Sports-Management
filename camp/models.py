from django.db import models
from club.models import Club

# Create your models here.
class Camp(models.Model):
    camp_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club=models.ForeignKey(Club,to_field='club_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    campname = models.CharField(max_length=50)
    incharge = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'camp'
