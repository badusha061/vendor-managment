from django.db import models

# Create your models here.


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True, blank=True)
    contact_datails = models.TextField(null=True,blank=True)
    vendor_code = models.CharField(max_length=10,unique=True,null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)


    def __str__(self) -> str:
        return self.name