from django.contrib import admin
from .models import CustomUser, Owner, Vendor, Affiliate, Delivery, Customer, Wholeseller, Delivery_address, BankDetails

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Owner)
admin.site.register(Vendor)
admin.site.register(Affiliate)
admin.site.register(Delivery)
admin.site.register(Wholeseller)
admin.site.register(Delivery_address)
admin.site.register(Customer)
admin.site.register(BankDetails)