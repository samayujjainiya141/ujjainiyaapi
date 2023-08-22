from django.contrib import admin 
from django.urls import path,include 
from rest_framework import routers 
from app.StudentViewset import StudentViewset 
router=routers.DefaultRouter() 
router.register(r'samay ujjainiya',StudentViewset) 
urlpatterns = [ 
    path('',include(router.urls)), 
    path('admin/',admin.site.urls) 
]