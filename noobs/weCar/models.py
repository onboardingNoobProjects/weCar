from django.db import models
from django.urls import reverse
import datetime


# Create your models here.
class Deal(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField(default='Insert deal description here')
    RRP = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    tippingPoint = models.IntegerField(default=0)
    expiry = models.DateTimeField(default=datetime.datetime(2020,1,1))
    pic = models.CharField(max_length=500, default='http://trotters-van-hire.co.uk/wp-content/uploads/2016/11/DelBoyVan.jpg')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        saving = ((self.RRP - self.price)/self.RRP)*100
        return self.title + ' - ' + str(round(saving, 2)) + '% off'
