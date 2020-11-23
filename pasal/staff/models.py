from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from shop.models import CustomUser, Vendor
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True) 
    slug = models.SlugField(max_length= 200, unique = True)
    created_by = models.ForeignKey(CustomUser, on_delete= models.PROTECT)
    image = models.ImageField(upload_to = 'category', blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_category", args=[self.slug])
class Brand(models.Model):
    brand_name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique = True)
    objects = models.Manager()
    class Meta:
        ordering = ('brand_name',)
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'
        
    def __str__(self):
        return self.brand_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)
    
class Sub_Category(models.Model):
    sub_name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique = True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    image = models.ImageField(upload_to = 'sub-category', blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ('sub_name',)
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'
        
    def __str__(self):
        return self.sub_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.sub_name)
        super(Sub_Category, self).save(*args, **kwargs)
        
    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_sub_category", args=[self.slug])
    
class Product(models.Model):    
    category = models.ForeignKey(Category, related_name= 'products', on_delete= models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, related_name='sub_category', on_delete=models.CASCADE, null = True)
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length=200, db_index= True)
    short = models.CharField(max_length = 400, null= True)
    commision = models.IntegerField(null = True)
    discount = models.IntegerField(null = True)
    tax = models.IntegerField(null = True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits= 20, decimal_places = 2)
    available_quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add= True)
    added_by = models.ForeignKey(CustomUser, related_name = 'added_by_user', on_delete=models.CASCADE)
    available = models.BooleanField(default= True)
    tags = TaggableManager()
    insurance = models.BooleanField(default= False)
    cashpayment = models.BooleanField(default=False)
    features = models.BooleanField(default=False)
    SKU = models.BigIntegerField(null = True)
    sale = models.CharField(max_length = 200, choices = (
        ('HotSale', 'Hot Sale'),
        ('FlashSale', 'Flash Sale'),
        ('ExclusiveSale', 'Exclusive Sale'),
        ('Normal', 'Normal')
    ), default = 'Normal')
    insurance = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, related_name='vendor_product', on_delete = models.PROTECT, null = True)
    sponsor = models.BooleanField(default=False)
    allovernepal = models.BooleanField(default=False)
    shippingarea = models.CharField(max_length = 1000, null = True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    
class insurance(models.Model):
    product_name = models.ForeignKey(Product, related_name='insurance_product', on_delete=models.PROTECT)
    fortime = models.CharField(max_length = 200, choices = (
        ('6','For 6 Month'),
        ('1', 'For One Year'),
        ('2', 'For Two Year'),
        ('3', 'For Three Year'),
        ('4', 'For 4 Years'),
        ('5', 'For 5 Years'),
        ('10', 'For 10 Years'),
        ('15', 'For 15 Years'),
        ('20', 'For 20 Years'),
    ))
    