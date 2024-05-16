
from django.urls import path
from .views import AddressList, AddressDetail

urlpatterns = [
    path('addresses/', AddressList.as_view(), name='address-list'),
    path('addresses/<int:pk>/', AddressDetail.as_view(), name='address-detail'),
]
