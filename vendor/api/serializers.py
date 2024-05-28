from rest_framework.serializers import ModelSerializer
from vendor.models import Vendor
from rest_framework.serializers import ValidationError


class CreateVendorSerilzers(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','name','contact_datails','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

    def validate_name(self, value):
        if  value is None:
            raise ValidationError("Vendor Name Cannot be Empty")
        elif len(value) < 3:
            raise ValidationError("Vendor Name Must be at least 3 characters long")
        return value


    def validate_contact_datails(self,values):
        if values is None:
            raise ValidationError("Vendor Contanct Datails is Cannot be Empty")
        return values
    

    def validate_vendorcode(self,values):
        
        if values is None:
            raise ValidationError("Vendor Cannot be Empty")
        try:
            instance = Vendor.objects.get(vendor_code = values)
            raise ValidationError("Vendor Code is Already Taken")
        except:
            pass
        return values

    def validate_on_time_delivery_rate(self,values):
        if values is None:
            raise ValidationError("Vendor Time Delivery Rate Cannot be Empty")
        
        elif values < 0 and values > 100:
            raise ValidationError("On-time Delivery Rate must be between 0 and 100")
        return values
    
    def validate_quality_rating_avg(self,values):
        if values is None:
            raise ValidationError("Vendor Qunatity rating average Cannot be empty")
        elif values < 0 or values > 10:  
            raise ValidationError("Quality Rating Average must be between 0 and 10")
        return values
    
    def validate_average_response_time(self,values):
        if values is None:
            raise ValidationError("Vendor Average Response Time Cannot be Empty")
        return values
    
    def validate_fulfillment_rate(self,values):
        if values is None:
            raise ValidationError("Vendor Fullfilment is Cannot be Empty")
        return values
    

    def validate(self, attrs):
        name = attrs.get('name')
        validated_name = self.validate_name(name)
        attrs['name'] = validated_name

        contact_datails = attrs.get('contact_datails')
        validated_name = self.validate_contact_datails(contact_datails)
        attrs['contact_datails'] = validated_name

        vendor_code = attrs.get('vendor_code')
        validated_name = self.validate_vendorcode(vendor_code)
        attrs['vendor_code'] = validated_name

        on_time_delivery_rate = attrs.get('on_time_delivery_rate')
        validated_name = self.validate_on_time_delivery_rate(on_time_delivery_rate)
        attrs['on_time_delivery_rate'] = validated_name

        
        quality_rating_avg = attrs.get('quality_rating_avg')
        validated_name = self.validate_quality_rating_avg(quality_rating_avg)
        attrs['quality_rating_avg'] = validated_name

        average_response_time = attrs.get('average_response_time')
        validated_name = self.validate_average_response_time(average_response_time)
        attrs['average_response_time'] = validated_name

        fulfillment_rate = attrs.get('fulfillment_rate')
        validated_name = self.validate_fulfillment_rate(fulfillment_rate)
        attrs['fulfillment_rate'] = validated_name

        return super().validate(attrs)
    

