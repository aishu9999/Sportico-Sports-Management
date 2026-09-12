from django.db import models
from trainer_register.models import TrainerRegister
from user_register.models import UserRegister
# from payment.models import Payment

# Create your models here.
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,to_field='user_id',on_delete=models.CASCADE)
    # trainer_id = models.IntegerField()
    trainer=models.ForeignKey(TrainerRegister,to_field='trainer_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    #payment_id = models.IntegerField()
    # payment=models.ForeignKey(Payment,to_field='payment_id',on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'appointment'
