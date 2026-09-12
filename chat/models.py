from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    trainer_id = models.IntegerField()
    message = models.CharField(max_length=30)
    sendertype = models.CharField(max_length=20)
    rectype = models.CharField(max_length=20)
    # date = models.DateField()
    # time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat'




