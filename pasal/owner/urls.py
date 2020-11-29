from django.urls import path
from .import views
app_name = 'owner'


urlpatterns = [
    path('', views.homepage, name= 'homepage'),
    path('addvendor', views.addvendor, name = 'addvendor'),
    path('adddeliveryboy', views.adddeliveryboy, name = 'adddeliveryboy'),
    path('addwholeseller', views.addwholeseller, name = 'addwholeseller'),
    path('vendorlist', views.allvendor, name = 'vendorlist'),
    path('sellerlist', views.sellerlist, name = 'sellerlist'),
    path('deliveryboylist', views.deliverylist, name = 'deliverylist'),
    path('affiliatelist', views.affiliatelist, name = 'affiliatelist'),
    path('userlist', views.userlist, name = 'userlist'),
    path('vendor_report/id=<int:id>', views.vendorreport, name = 'vendorreport'),
    path('wholesellerreport/id=<int:id>', views.wholesellerReport, name = 'wholesellerReport'),
    path('kycrequest', views.kycrequest, name = 'kycrequest'),
    path('verifyvendor/<int:id>', views.verifyVendor, name='verifyVendor'),
    path('verifywholeseller/<int:id>', views.verifySeller, name='verifySeller'),
    
]