from django.db import models
from shop.models import Shop
from payment.models import Payment
from user_register.models import UserRegister
from items.models import Product

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    #shop_id = models.IntegerField()
    shop = models.ForeignKey(Shop, to_field='shop_id', on_delete=models.CASCADE)
    #product_id = models.IntegerField()
    product = models.ForeignKey(Product, to_field='product_id', on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegister,to_field='user_id',on_delete=models.CASCADE)
    # payment_id = models.IntegerField()
    payment=models.ForeignKey(Payment,to_field='payment_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'order'
