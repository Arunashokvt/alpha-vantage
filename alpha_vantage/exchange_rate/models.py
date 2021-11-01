from django.db import models

# Create your models here.

class Exchange(models.Model):
    from_currency= models.CharField(max_length=50)
    from_currency_name = models.CharField(max_length=50)
    to_currency= models.CharField(max_length=50)
    to_currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=30,decimal_places=10)
    las_refreshed= models.DateTimeField()
    time_zone = models.CharField(max_length=10)
    bid_price = models.DecimalField(max_digits=30,decimal_places=10)
    ask_price = models.DecimalField(max_digits=30,decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.from_currency+' to ' + self.to_currency
    
