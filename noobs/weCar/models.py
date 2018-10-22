from django.db import models

# Create your models here.
class Deal(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField
    RRP = models.IntegerField
    price = models.IntegerField
    tippingPoint = models.IntegerField
    expiry = models.DateTimeField
    pic = models.ImageField
