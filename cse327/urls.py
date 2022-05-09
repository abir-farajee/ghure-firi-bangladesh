#.....cse327 URL Configuration............."""




from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('account/',include('account.urls')),
    path('explore/',include('explore.urls')),
    path('webadmin/',include('webadmin.urls')),
    path('package/',include('package.urls')),
    path('tour/',include('tour.urls')),
    path('',views.index),
    path('main',views.main),
    path('img',views.img),
    path('admin/', admin.site.urls),
    
]
