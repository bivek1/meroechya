from django.shortcuts import render
from .forms import AddCat, AddSubCat, AddBrand
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shop.forms import VendorForm, DeliveryBoyForm, WholeSellerForm
from shop.models import CustomUser, Vendor, Wholeseller, Customer, Affiliate, Delivery
from owner.models import verifyrequest
# Create your views here.
def userdashboard(request):
    current = CustomUser.objects.get(id = request.user.id)
    
    dist = {
        'man': current,
    }
    return render(request, 'user/userboard.html', dist)

def vendordashboard(request):
    current = CustomUser.objects.get(id = request.user.id)
        
    dist = {
        'man': current,
    }
    return render(request, 'vendor/vendorboard.html', dist)
    
def deliverdashboard(request):
    current = CustomUser.objects.get(id = request.user.id)
    
        
    dist = {
        'man': current,
    }
    return render(request, 'delivery/deliverydashboard.html', dist)

def affiliatedashboard(request):
    current = CustomUser.objects.get(id = request.user.id)
        
    dist = {
        'man': current,
    }
    return render(request, 'affiliate/affiliateboard.html', dist)

def wholesellerdashboard(request):
    current = CustomUser.objects.get(id = request.user.id)
        
    dist = {
        'man': current,
    }
    return render(request, 'wholeseller/sellerboard.html', dist)
    
    
def addmanage(request):
    
    return render(request, 'admin/addmanage.html')

def add_category(request):
    form = AddCat(request.POST or None)
    dist = {
        'form': form,
        
    }
    if form.is_valid():
        form = AddCat(request.POST, request.FILES)
        try:
            savedata = form.save(commit = False)
            savedata.created_by = request.user
            savedata.save()
        except:
            messages.error(request, 'Category slug match. It has been added already')
            return render(request, 'staff/addcategory.html', dist)
        # return HttpResponseRedirect(reverse('shop:all_services'))
        return HttpResponse('Category Added Sucessfully')
    else:
        return render(request, 'staff/addcategory.html', dist)
    return render(request, 'staff/addcategory.html', dist)

def addsubcat(request):
    form = AddSubCat(request.POST or None)
    dist = {
        'form': form,
    }
    if form.is_valid():
        form = AddSubCat(request.POST, request.FILES)
        try:
            form.save()
        except:
            messages.error(request, 'Something wrong can not add sub category')
            return render(request, 'staff/addsubcat.html', dist)
        return HttpResponse('Sub Category Added Sucessfully')
    else:
        return render(request, 'staff/addsubcat.html', dist)
    return render(request, 'staff/addsubcat.html', dist)

def addbrand(request):
    form = AddBrand(request.POST or None)
    dist = {
        'form': form,
    }
    if form.is_valid():
        form = AddBrand(request.POST)
        try:
            form.save()
        except:
            messages.error(request, 'Something wrong can not add brand')
            return render(request, 'staff/addbrand.html', dist)
        return HttpResponse('Brand Added Sucessfully')
    else:
        return render(request, 'staff/addbrand.html', dist)
    return render(request, 'staff/addbrand.html', dist)

        
def vendorkyc(request):
    if request.method == 'POST':
        usoo = request.user
        print(usoo)
        user_obj = CustomUser.objects.get(id = usoo.id)
        print(user_obj)
        number = request.POST['number']
        vat = request.POST['vat']
        kyc = request.FILES['kyc']
        tax_pic = request.FILES['tax']
        
        aa = user_obj.vendor
        print(aa)
        aa.number = number
        aa.vat = vat
        aa.KYC = kyc
        aa.taxpic = tax_pic
        aa.save()
        
        requester = verifyrequest()
        requester.requester = request.user
        requester.save()
        messages.success(request, 'Your KYC details has been sent')
        return HttpResponseRedirect(reverse('staff:vendordashboard'))
    else:
        return render(request, 'vendor/kyc.html')