from django.db import models
from club.models import Club

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    #club_id = models.IntegerField()
    club = models.ForeignKey(Club, to_field='club_id', on_delete=models.CASCADE)
    notification = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'notification'
