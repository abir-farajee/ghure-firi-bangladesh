
from django.urls import path, include
from . import views

urlpatterns = [
 path('addpackage',views.addpackage, name="addpackage"),
 path('adminlog',views.adminlog, name="adminlog"),
 path('adminhome',views.adminhome, name="adminhome"),
 path('adminlogout',views.adminlogout, name="adminlogout"),
 path('addtour',views.addtour, name="addtour"),
 path('addhotel',views.addhotel, name="addhotel"),
 path('packagelist',views.packagelist, name="packagelist"),
 path('updatepack',views.updatepack, name="updatepack"),
 path('deletepack',views.deletepack, name="deletepack"),
 path('deletetour',views.deletetour, name="deletetour"),
 path('tourlist',views.tourlist, name="tourlist"),
 path('packbooked',views.packbooked, name="packbooked"),
 path('tourbooked',views.tourbooked, name="tourbooked"),
 path('recheckreq',views.recheckreq, name="recheckreq"),
 path('comfirmtourbooking',views.comfirmtourbooking, name="comfirmtourbooking"),
 path('packrecheckreq',views.packrecheckreq, name="packrecheckreq"),
 path('packcomfirmtourbooking',views.packcomfirmtourbooking, name="packcomfirmtourbooking"),
 
 path('addtransportation',views.addtransportation, name="addtransportation"),

 
] 