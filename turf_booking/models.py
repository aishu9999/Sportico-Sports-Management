from django.db import models
from user_register.models import UserRegister
from club.models import Club
from location.models import Location
from time_info.models import TimeInfo
from turf_register.models import TurfRegister

# Create your models here.
class TurfBooking(models.Model):
    turfbooking_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,to_field='user_id',on_delete=models.CASCADE)
    #club_id = models.IntegerField()
    # club = models.ForeignKey(Club, to_field='club_id', on_delete=models.CASCADE)
    # turf_id = models.IntegerField()
    turf=models.ForeignKey(TurfRegister,to_field='turf_id',on_delete=models.CASCADE)
    #location_id = models.IntegerField()
    # location = models.ForeignKey(Location, to_field='location_id', on_delete=models.CASCADE)
    #time_id = models.TimeField()
    # time = models.ForeignKey(TimeInfo, to_field='time_id', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'turf_booking'

