from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('addtocart/',views.CartAddView.as_view(), name='addtocart'),
    path('fooddetails/<int:pk>/',views.food_details, name='food_details'),
    path('cartdetails/',views.cart_details, name='cart_details'),
    path('delete/<int:pk>/',views.DeleteCartView.as_view(), name='delete_cart'),
    path('ordercreation/',views.OrderCreateView.as_view(), name='order_creation'),
    path('orderdetails/<int:pk>/',views.OrderDetailView.as_view(), name='order_details'),
    path('myorders/',views.MyOrdersView.as_view(), name='myorders'),
    path('paidorders/',views.PaidOrdersView.as_view(), name='paidorders'),
    path('orderinfopaymented/<int:pk>/',views.OrdersInfo.as_view(), name='myorderspay'),
    path('undoorder/<int:pk>/',views.undo_orders, name='undo_orders'),
]
