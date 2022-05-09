
from django.urls import path, include
from . import views

urlpatterns = [
 path('allpackage',views.allpackage, name="allpackage"),
 path('searchbylocation',views.searchbylocation, name="searchbylocation"),
 path('searchbyprice',views.searchbyprice, name="searchbyprice"),
 path('addstar',views.addstar,name='addstar'),
 path('removestar',views.removestar,name='removestar'),
 path('booking',views.booking, name="booking"),
 path('sendmsgpack',views.sendmsgpack, name="sendmsgpack"),
 path('packpaymentverify',views.packpaymentverify, name="packpaymentverify"),

 
] 