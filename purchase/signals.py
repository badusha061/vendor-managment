from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, HistoricalPerformance, Vendor
from django.db.models import Avg, F, ExpressionWrapper, fields

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    vendor = instance.vendor

    total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    on_time_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=F('order_date')).count()
    on_time_delivery_rate = (on_time_orders / total_completed_orders) * 100 if total_completed_orders else 0


    quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, status='completed').aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0


    response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).annotate(
        response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())
    ).aggregate(avg_response=Avg('response_time'))
    average_response_time = response_times['avg_response'].total_seconds() if response_times['avg_response'] else 0


    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfillment_rate = (fulfilled_orders / total_orders) * 100 if total_orders else 0

   
    historical_performance, created = HistoricalPerformance.objects.get_or_create(
        vendor=vendor,
        defaults={
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate
        }
    )

    if not created:
        historical_performance.on_time_delivery_rate = on_time_delivery_rate
        historical_performance.quality_rating_avg = quality_rating_avg
        historical_performance.average_response_time = average_response_time
        historical_performance.fulfillment_rate = fulfillment_rate
        historical_performance.save()
