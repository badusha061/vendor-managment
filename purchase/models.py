from django.db import models
from vendor.models import Vendor
# Create your models here.

STATUS_CHOICES = (
    ('pending','Pending'),
    ('completed','Completed'),
    ('canceled','Canceled'),

)


class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    po_name = models.CharField(max_length=50, unique=True, null=True,blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True,blank=True)
    delivery_date = models.DateTimeField(null=True,blank=True)
    items = models.JSONField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(verbose_name="Issue Date", auto_now_add=True)
    acknowledgment_date = models.DateTimeField(verbose_name="Acknowledgment Date", null=True, blank=True)

    def __str__(self) -> str:
        return self.po_name
    


class HistoricalPerformance(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return self.vendor

