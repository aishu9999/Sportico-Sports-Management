from django.db import models

# Create your models here.
class UserRegister(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    height = models.IntegerField()
    weight = models.IntegerField()
    physical = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_register'
