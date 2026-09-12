from django.db import models
from user_register.models import UserRegister
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,to_field='user_id' ,on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'payment'

