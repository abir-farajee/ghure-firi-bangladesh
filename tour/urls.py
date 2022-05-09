
from django.urls import path, include
from . import views

urlpatterns = [
 path('all',views.all, name="all"),
 path('tourdetails',views.tourdetails, name="tourdetails"),
 path('booking',views.booking, name="booking"),
 path('sendmsg',views.sendmsg, name="sendmsg"),
 path('tourpaymentverify',views.tourpaymentverify, name="tourpaymentverify"),
 path('mail',views.mail, name="mail"),
 

 
] 