from django.urls import path
from .views import Create_Vendor ,  Retrieve_Update_Destroy ,Vendor_Perfomance

urlpatterns = [
    #Listing (GET)- Creating(POST) Vendors
    path('vendors/', Create_Vendor.as_view(), name='create-vendor'),

    #Retrieve a specific vendor's details (GET) ,  Update a vendor's details (PUT) ,  Delete a vendor(DELTE)
    path('vendors/<int:pk>/', Retrieve_Update_Destroy.as_view(), name='update-delete-edit-vendor'),


    path('vendors/<int:pk>/performance', Vendor_Perfomance.as_view(), name='update-delete-edit-vendor'),
]
