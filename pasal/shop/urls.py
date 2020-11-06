from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('dologin', views.dologin, name = 'dologin'),
    path('logout',views.logout_user, name = "logout" ),
    path('joinasvendor', views.enrollvendor, name = 'enrollvendor'),
    path('joinaswholeseller', views.enrollwholeseller, name = 'enrollseller'),
]
