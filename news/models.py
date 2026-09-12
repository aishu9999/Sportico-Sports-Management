from django.db import models

# Create your models here.
class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    time = models.TimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'news'
