from django.db import models
from shop.models import Shop
# Create your models here.
class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    #shop_id = models.IntegerField()
    shop=models.ForeignKey(Shop,to_field='shop_id',on_delete=models.CASCADE)
    review_of_item = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'items'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    # shop_id = models.IntegerField()
    shop = models.ForeignKey(Shop, to_field='shop_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    rentpurchase = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'product'

