from django.urls import path
from .import views

app_name = 'staff'

urlpatterns = [
    path('userdashboard', views.userdashboard, name= 'userdashboard'),
    path('vendordashboard', views.vendordashboard, name = 'vendordashboard'),
    path('wholesellerdashboard', views.wholesellerdashboard, name= 'wholesellerdashboard'),
    path('affiliatedashboard', views.affiliatedashboard, name= 'affliliatedashboard'),
    path('deliverydashboard', views.deliverdashboard, name = 'deliverydashboard'),
    path('addmanageservices', views.addmanage, name = 'addmanage'),
    path('addcategory', views.add_category, name = 'add_category'),
    path('addsubcategory', views.addsubcat, name = 'add_sub_cat'),
    path('addbrand', views.addbrand, name = 'add_brand'),
    path('verifykyc', views.vendorkyc, name = 'vendorkyc'),
]
