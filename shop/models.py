from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    rating = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'shop'


