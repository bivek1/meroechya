from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.



class CustomUser(AbstractUser):
    user_type_data = (('1','Admin'), ('2', 'Wholeseller'), ('3', 'vendor'), ('4', 'Delivery'), ('5', 'Affiliate'),('6', 'customer'))
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 20)
    
class Owner(models.Model):
    id = models.AutoField(primary_key = 1)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    profile = models.ImageField(upload_to = 'Admin_Profile', blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.admin.email

class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal', null = True)  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu', null = True)
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField(null = True)
    street = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(upload_to = "Vendor_Profile", blank = True, null = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    KYC = models.ImageField(upload_to = 'KYC', blank = True, null = True)
    verified = models.BooleanField(default=False)
    citizen_number = models.BigIntegerField(null = True)
    DOB = models.DateField(null = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    permanent_district = models.CharField(max_length = 200, null = True)
    permanent_muncipalicity = models.CharField(max_length = 200, null = True)
    permanent_address = models.CharField(max_length = 200, null = True)
    permanent_ward = models.CharField(max_length = 200, null = True)
    objects = models.Manager()
 
    def __str__(self):
        return self.fullname
class Wholeseller(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = 'wholeseller')
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal')  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu')
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField()
    street = models.CharField(max_length = 200)
    shopname = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to = "Wholeseller_Profile", blank = True)
    KYC = models.ImageField(upload_to = 'KYC', blank = True)
    vat = models.CharField(max_length = 200, null = True)
    taxpic = models.ImageField(upload_to = 'TaxClear',blank = True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.fullname
    
    def get_absolute_url(self):
        return reverse("owner:wholesellerReport", args=[self.id])
    

class Vendor(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal')  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu')
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField()
    street = models.CharField(max_length = 200)
    companyname = models.CharField(max_length = 200)
    profile_pic = models.ImageField(upload_to = "Vendor_Profile", blank = True)
    vat = models.CharField(max_length = 200, null = True)
    taxpic = models.ImageField(upload_to = 'TaxClear',blank = True)
    KYC = models.ImageField(upload_to = 'KYC', blank = True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.fullname
    def get_absolute_url(self):
        return reverse("owner:vendorreport", args=[self.id])


class Affiliate(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal')  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu')
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField()
    street = models.CharField(max_length = 200)
    profile_pic = models.ImageField(upload_to = "Vendor_Profile", blank = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    verified = models.BooleanField(default=False)
    citizen_number = models.BigIntegerField(null = True)
    DOB = models.DateField(null = True)
    citizenimg = models.ImageField(upload_to = 'aff', blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    permanent_district = models.CharField(max_length = 200, null = True)
    permanent_muncipalicity = models.CharField(max_length = 200, null = True)
    permanent_address = models.CharField(max_length = 200, null = True)
    permanent_ward = models.CharField(max_length = 200, null = True)
    objects = models.Manager()
    
    def __str__(self):
        return self.fullname

class Delivery(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal')  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu')
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField()
    street = models.CharField(max_length = 200)
    profile_pic = models.ImageField(upload_to = "Vendor_Profile", blank = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    DOB = models.DateField(null = True)
    vechile_no = models.CharField(max_length = 200)
    vechile_color = models.CharField(max_length = 200)
    vechile_name = models.CharField(max_length = 200)
    license_no = models.CharField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    permanent_country = models.CharField(max_length = 200, null = True)
    permanent_district = models.CharField(max_length = 200, null = True)
    permanent_address = models.CharField(max_length = 200, null = True)
    permanent_muncipalicity = models.CharField(max_length = 200, null = True)
    permanent_ward = models.CharField(max_length = 200, null = True)
    permanent_tole = models.CharField(max_length = 200, null = True)
    objects = models.Manager()
    
    def __str__(self):
        return self.fullname


class Delivery_address(models.Model):
    master = models.ForeignKey(Customer, related_name='deliveryaddress', on_delete=models.PROTECT)
    fullname = models.CharField(max_length = 200)
    number = models.BigIntegerField(null = True)
    region = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    Area = models.CharField(max_length = 100)
    objects = models.Manager()

class BankDetails(models.Model):
    ven = models.ForeignKey(Vendor, related_name='vendor_bank', on_delete=models.PROTECT, null = True, blank = True)
    use = models.ForeignKey(Affiliate, related_name='aff_bank', on_delete=models.PROTECT, null = True, blank = True) 
    acc_no = models.CharField(max_length = 300)
    acc_name = models.CharField(max_length = 300)
    bank_name = models.CharField(max_length = 300)
    bank_branch = models.CharField(max_length = 200)


@receiver(post_save, sender= CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Owner.objects.create(admin = instance)
        if instance.user_type == 2:
            Wholeseller.objects.create(admin = instance)
        if instance.user_type == 3: 
            Vendor.objects.create(admin = instance)
        if instance.user_type == 4: 
            Delivery.objects.create(admin = instance)
        if instance.user_type == 5: 
            Affiliate.objects.create(admin = instance)
        if instance.user_type == 6: 
            Customer.objects.create(admin = instance)
            
@receiver(post_save, sender=CustomUser)
def _post_save_receiver(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.owner.save()
    if instance.user_type == 2:
        instance.wholeseller.save()
    if instance.user_type == 3:
        instance.vendor.save()
    if instance.user_type == 4:
        instance.delivery.save()
    if instance.user_type == 5:
        instance.affiliate.save()
    if instance.user_type == 6:
        instance.customer.save()