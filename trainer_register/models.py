from django.db import models

# Create your models here.
class TrainerRegister(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    field = models.CharField(max_length=50)
    time_info = models.TimeField()
    payment = models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'trainer_register'


class UploadedVideo(models.Model):
    video_id = models.AutoField(primary_key=True)
    video = models.CharField(max_length=100)
    # trainer_id = models.IntegerField()
    trainer=models.ForeignKey(TrainerRegister,to_field='trainer_id',on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'uploaded_video'


