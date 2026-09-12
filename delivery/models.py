from django.db import models
from shop.models import Shop
from order.models import Order
# Create your models here.
class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    # shop_id = models.IntegerField()
    shop=models.ForeignKey(Shop,to_field='shop_id',on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    user_id = models.IntegerField()
    # order_id = models.IntegerField()
    order=models.ForeignKey(Order,to_field='order_id',on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'delivery'
