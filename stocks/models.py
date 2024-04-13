from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Stocks(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=None)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Stock"

class Trade(models.Model):
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=10)
    stock = models.ForeignKey(Stocks, default=None, null=True, blank=True, on_delete=models.CASCADE)
    quantity =  models.IntegerField(null=True,blank=True,default=None)

    def __str__(self):
        return self.stock.name

    def __unicode__(self):
        return self.stock.name

    class Meta:
        verbose_name = "Trade"

class Qoute(models.Model):
    author = models.CharField(max_length=50)
    quote = models.CharField(max_length=500)

    def __str__(self):
        return self.quote

    def __unicode__(self):
        return self.quote

    class Meta:
        verbose_name = "Qoute"
