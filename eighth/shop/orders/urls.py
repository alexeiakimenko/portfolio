from django.urls import path
from .views import OrderCreateView, full_order, OrderListView, OrderDetailView

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
    path('full_order/', full_order, name='full_order'),
]
