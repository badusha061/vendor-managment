from rest_framework.generics import   ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import CreateVendorSerilzers
from vendor.models import Vendor
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .pagination import ListVendorSetPagination
from rest_framework.views import APIView
from purchase.models import HistoricalPerformance
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK , HTTP_204_NO_CONTENT



@permission_classes([IsAuthenticated])
class Create_Vendor(ListCreateAPIView):
    serializer_class = CreateVendorSerilzers
    pagination_class = ListVendorSetPagination
    queryset = Vendor.objects.all()


@permission_classes([IsAuthenticated])
class Retrieve_Update_Destroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateVendorSerilzers
    queryset = Vendor.objects.all()


# @permission_classes([IsAuthenticated])
class Vendor_Perfomance(APIView):
    def get(self,request,pk):
        try:
            vendor_instance  = HistoricalPerformance.objects.get(vendor = pk)
            
            data = {
                'on_time_delivery_rate': vendor_instance.on_time_delivery_rate,
                'quality_rating_avg': vendor_instance.quality_rating_avg,
                'average_response_time': vendor_instance.average_response_time,
                'fulfillment_rate': vendor_instance.fulfillment_rate
            }
            return Response(data=data,status=HTTP_200_OK)
        except Exception as e:
            data = {
                "error":"Vendors is Not Found"
            }
            return Response(data=data,status= HTTP_204_NO_CONTENT)