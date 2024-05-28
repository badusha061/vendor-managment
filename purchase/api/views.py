from .serializers import PurchaseOrderSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from purchase.models import PurchaseOrder
from .pagination import PurchaseOrderSetPagination
from rest_framework import filters
from vendor.models import Vendor
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST , HTTP_200_OK , HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.utils import timezone



@permission_classes([IsAuthenticated])
class Create_PurchaseOrder(ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer
    pagination_class = PurchaseOrderSetPagination
    search_fields = ['vendor__name']
    filter_backends = [filters.SearchFilter]
    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_name = self.request.query_params.get('vendor_name')
        if vendor_name:
            queryset = queryset.filter(vendor__name__icontains = vendor_name)
        return queryset



@permission_classes([IsAuthenticated])
class Retrieve_Update_Destroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()



# @permission_classes([IsAuthenticated])
class UpdateAcknowledgment(APIView):
    def post(self, request, po_id):
        try:
            po = PurchaseOrder.objects.get(id=po_id)
            if po.acknowledgment_date:
                return Response({"error": "Purchase order already acknowledged"}, status=HTTP_400_BAD_REQUEST)
                
            po.acknowledgment_date = timezone.now()
            po.save()

            vendor = po.vendor
            all_acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
            total_response_time = sum([(po.acknowledgment_date - po.issue_date).total_seconds() for po in all_acknowledged_pos])
            vendor.average_response_time = total_response_time / len(all_acknowledged_pos) if all_acknowledged_pos else 0
            vendor.save()

            return Response({"message": "Purchase order acknowledged successfully"}, status=HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            raise NotFound("Purchase Order not found")
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)