from django.db import models
from shop.models import CustomUser
# Create your models here.
class verifyrequest(models.Model):
    requester = models.ForeignKey(CustomUser, related_name = 'verifyRequest', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add= True)