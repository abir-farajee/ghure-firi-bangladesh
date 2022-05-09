
from django.urls import path, include
from . import views

urlpatterns = [
 path('addexplore',views.addexplore, name="addexplore"),
 path('explore',views.explore,name='explore'),
 path('addlike',views.addlike,name='addlike'),
 path('unlike',views.unlike,name='unlike'),

 path('post_check',views.post_check,name="post_check"),

 
] 