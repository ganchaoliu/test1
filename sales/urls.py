from django.urls import path

from sales import views

urlpatterns = [
    path('orders/', views.listorders),
    path('customers/', views.listcustomers),
]