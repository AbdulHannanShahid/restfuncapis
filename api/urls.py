from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
   path('', views.index, name="home" ),
   path('apicheck/', views.api_check, name="apiviews" ),
   path('apiusers/', views.api_users, name="apiusers" ),
   path('apicreateuser/', views.api_createuser, name="apicreateuser" ),
   path('apiuserdetails/<int:pk>/', views.api_userdetails, name="apiusersdetails" ),
   path('apiuserupdate/<int:id>/', views.api_updateuser, name="apiuserupdate" ),
   path('apiuserdelete/<int:id>/', views.api_deleteuser, name="apiuserdelete" ),
]