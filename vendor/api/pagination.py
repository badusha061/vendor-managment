from rest_framework.pagination import PageNumberPagination

    
class ListVendorSetPagination(PageNumberPagination):
    page_size = 3
    page_query_param  = 'page'
    max_page_size = 1000

