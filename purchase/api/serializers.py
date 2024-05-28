from purchase.models import PurchaseOrder
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError


class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id','po_name','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']

    def validate_po_name(self,values):
        if values is None:
            raise ValidationError("Product Order Name is Cannot be Empty")
        elif len(values) < 3:
            raise ValidationError("Product Order Name Must be More than 3 letters")
        return values
    
    def validate_vendor(self,values):
        if values is None:
            raise ValidationError("Vendor Cannot be Empty")
        return values
    

    def validate_order_date(self,value):
        if value is None:
            raise ValidationError("Order Date Cannot be Empty")
        return value
    

    def validate_delivery_date(self,value):
        if value is None:
            raise ValidationError("Deilvery Date Cannot be Empty")
        return value
    
    def validate_items(self,value):
        if value is None:
            raise ValidationError("Items Cannot be Empty")
        return value
    
    def validate_quantity(self,value):
        if value is None:
            raise ValidationError("Quantity Cannot be Empty")
        elif value == 0:
            raise ValidationError("Quantity Cannot be 0 More than 1")
        return value
    
    def validate_status(self,value):
        if value is None:
            raise ValidationError("Status Cannot be Empty")
        return value
    
    def validate_quality_rating(self,value):
        if value is None:
            raise ValidationError("Quantity Rating Cannot be Empty")
        return value
    
    def validate_issue_date(self,value):
        if value is None:
            raise ValidationError("Issue Date Cannot be Empty")
        return value
    

    def validate_acknowledgment_date(self,value):
        if value is None:
            raise ValidationError("Date Cannot be Empty")
        return value

    def validate(self, attrs):

        po_name = attrs.get("po_name")
        validated_name = self.validate_po_name(po_name)
        attrs['po_name'] = validated_name


        vendor = attrs.get("vendor")
        validated_name = self.validate_vendor(vendor)
        attrs['vendor'] = validated_name

        
        order_date = attrs.get("order_date")
        validated_name = self.validate_order_date(order_date)
        attrs['order_date'] = validated_name


        delivery_date = attrs.get("delivery_date")
        validated_name = self.validate_delivery_date(delivery_date)
        attrs['delivery_date'] = validated_name

        items = attrs.get("items")
        validated_name = self.validate_items(items)
        attrs['items'] = validated_name

        quantity = attrs.get("quantity")
        validated_name = self.validate_quantity(quantity)
        attrs['quantity'] = validated_name

        status = attrs.get("status")
        validated_name = self.validate_status(status)
        attrs['status'] = validated_name

        quality_rating = attrs.get("quality_rating")
        validated_name = self.validate_quality_rating(quality_rating)
        attrs['quality_rating'] = validated_name

        issue_date = attrs.get("issue_date")
        validated_name = self.validate_issue_date(issue_date)
        attrs['issue_date'] = validated_name

        acknowledgment_date = attrs.get("acknowledgment_date")
        validated_name = self.validate_acknowledgment_date(acknowledgment_date)
        attrs['acknowledgment_date'] = validated_name

        return super().validate(attrs)