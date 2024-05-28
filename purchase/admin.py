from django.contrib import admin
from .models import PurchaseOrder, HistoricalPerformance
# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)



