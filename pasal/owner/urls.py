from django.urls import path
from .import views
app_name = 'owner'


urlpatterns = [
    path('', views.homepage, name= 'homepage'),
    path('addvendor', views.addvendor, name = 'addvendor'),
    path('vendorlist', views.allvendor, name = 'vendorlist'),
    path('vendor_report/id=<int:id>', views.vendorreport, name = 'vendorreport')
    
]