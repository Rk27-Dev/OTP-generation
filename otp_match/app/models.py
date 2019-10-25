from django.db import models

# Create your models here.
class otpmodel(models.Model):
    name=models.CharField(max_length=20)
    Contact_no=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    conform_password=models.CharField(max_length=20)
    otps=models.IntegerField(default=0)