from django.db import models
from club.models import  Club
from camp.models import Camp
from location.models import Location
from time_info.models import TimeInfo
from payment.models import Payment
from user_register.models import UserRegister

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    #club_id = models.IntegerField()
    club=models.ForeignKey(Club,to_field='club_id',on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,to_field='user_id',on_delete=models.CASCADE)
    #camp_id = models.IntegerField()
    camp=models.ForeignKey(Camp,to_field='camp_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    # location_id = models.IntegerField()
    # location=models.ForeignKey(Location,to_field='location_id',on_delete=models.CASCADE)
    #time_id = models.IntegerField()
    # time=models.ForeignKey(TimeInfo,to_field='time_id',on_delete=models.CASCADE)
    #payment_id = models.IntegerField()
    # payment=models.ForeignKey(Payment,to_field='payment_id',on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'booking'
