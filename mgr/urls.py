
from django.urls import path

from mgr import customer, medicine, order
from mgr import sign_in_out

urlpatterns = [
    path('customers', customer.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    path('medicines', medicine.dispatcher),
    path('orders', order.dispatcher),
]