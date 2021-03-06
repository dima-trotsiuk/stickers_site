from django.urls import path, include

from .bag_api.urls import bag_patterns
from .storage_api.urls import product_patterns
from .order_management_api.urls import order_patterns
from .search_for_ttn_api.urls import ttn_patterns


urlpatterns = [
    path('v1/storage/', include(product_patterns)),
    path('v1/bag/', include(bag_patterns)),
    path('v1/order/', include(order_patterns)),
    path('v1/search/', include(ttn_patterns)),
]

