
from django.urls import path, include
from . import views

urlpatterns = [
 path('signup',views.signup, name="signup"),
 path('login',views.login, name="login"),
 path('img',views.img, name="img"),
 path('profile',views.profile, name="profile"),
 path('update_profile',views.update_profile,name="update_profile"),
 path('logout',views.logout, name="logout"),
 path('pass_reset',views.pass_reset, name="pass_reset"),
 path('deletepost',views.deletepost, name="deletepost"),
 path('mybooking',views.mybooking, name="mybooking"),
 path('ticket',views.ticket, name="ticket"),
 path('googlelogin',views.googlelogin, name="googlelogin"),

 path('packticket',views.packticket, name="packticket"),
 
]
