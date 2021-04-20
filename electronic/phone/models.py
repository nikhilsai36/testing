from django.db import models

# Create your models here.
class Phone(models.Model):
    Name = models.CharField(max_length=15, null=True)
    ModelNo = models.CharField(max_length=15, null=True)
    IMEINo = models.IntegerField()
    DOM = models.DateField()



