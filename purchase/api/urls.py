from django.urls import path
from .views import Create_PurchaseOrder ,  Retrieve_Update_Destroy , UpdateAcknowledgment

urlpatterns = [

    #Listing (GET) - Creating(POST) Purchase Order
    path('purchase_orders/', Create_PurchaseOrder.as_view(), name='create-pruchaseorder'),

    #Retrieve a specific Purchase Order details (GET) ,  Update a Purchase Order details (PUT) ,  Delete a Purchase Order(DELTE)
    path('purchase_orders/<int:pk>/', Retrieve_Update_Destroy.as_view(), name='update-delete-edit-pruchaseorder'),


    path('pruchase_orders/<int:pk>/acknowledge', UpdateAcknowledgment.as_view(), name='update-acknowledgment'),
]
