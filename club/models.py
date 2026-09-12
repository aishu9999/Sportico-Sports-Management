from django.db import models

# Create your models here.
class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    clubname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    head = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    email_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'club'

