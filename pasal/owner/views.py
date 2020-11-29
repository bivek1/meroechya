from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from shop.forms import VendorForm, DeliveryBoyForm, WholeSellerForm
from shop.models import CustomUser, Vendor, Wholeseller, Customer, Affiliate, Delivery
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import verifyrequest
from django.contrib import messages
# Create your views here.


@login_required 
def homepage(request):
    verifyC = verifyrequest.objects.all().count()
    print(verifyC)
    dist = {
        'vc': verifyC
    }
    return render(request, 'admin/dashboard.html', dist)

def addvendor(request):
    form = VendorForm(request.POST or None)
    
    if form.is_valid():
        foms = VendorForm(request.POST)
        cd = form.cleaned_data
        fullname = cd['fullname']
        email = cd['email']
        password = cd['password']
        country = cd['country']
        district = cd['district']
        province = cd['province']
        ward_no = cd['ward_no']
        street = cd['street']
        company = cd['companyname']
       
        fom = foms.save(commit=False)
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '3')
        fom.admin = vend
        fom.fullname = fullname
        fom.country = country
        fom.district = district
        fom.province = province
        fom.ward_no = ward_no
        fom.street = street
        fom.companyname = company
        fom.save()    
        return HttpResponseRedirect(reverse('owner:vendorlist'))
    else:
        return render(request, 'admin/addvendor.html', {'form':form})
    
    return render(request, 'admin/addvendor.html', {'form':form})

def allvendor(request):
    vendorlist = Vendor.objects.all()
    return render(request, 'admin/vendorlist.html', {'list' : vendorlist})

def sellerlist(request):
    vendorlist = Wholeseller.objects.all()
    return render(request, 'admin/sellerlist.html', {'list' : vendorlist})

def deliverylist(request):
    vendorlist = Delivery.objects.all()
    return render(request, 'admin/deliveryboylist.html', {'list' : vendorlist})

def affiliatelist(request):
    vendorlist = Affiliate.objects.all()
    return render(request, 'admin/affiliatelist.html', {'list' : vendorlist})

def userlist(request):
    vendorlist = Customer.objects.all()
    return render(request, 'admin/userlist.html', {'list' : vendorlist})

def vendorreport(request , id):
    selected = get_object_or_404(Vendor, id = id)
    return render(request, 'admin/vendorreport.html', {'one': selected, 'id':id})
    
def wholesellerReport(request, id):
    selected = get_object_or_404(Wholeseller, id = id)
    return render(request, 'admin/wholesellerreport.html', {'one': selected, 'id':id})
def adddeliveryboy(request):
    
    form = DeliveryBoyForm(request.POST or None)
    
    if form.is_valid():
        foms = DeliveryBoyForm(request.POST)
        cd = form.cleaned_data
        fullname = cd['fullname']
        email = cd['email']
        password = cd['password']
        country = cd['country']
        district = cd['district']
        province = cd['province']
        ward_no = cd['ward_no']
        street = cd['street']
        gender = cd['gender']
        dob = cd['DOB']
        vechile_no = cd['vechile_no']
        vechile_color = cd['vechile_color']
        vechile_name = cd['vechile_name']
        license_no = cd['license_no']
        permanent_country = cd['permanent_country']
        permanent_district = cd['permanent_district']
        permanent_address = cd['permanent_address']
        permanent_muncipalicity = cd['permanent_muncipalicity']
        permanent_ward = cd['permanent_ward']
        permanent_tole = cd['permanent_tole']
        
        fom = foms.save(commit=False)
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '4')
        fom.admin = vend
        fom.fullname = fullname
        fom.country = country
        fom.district = district
        fom.province = province
        fom.ward_no = ward_no
        fom.street = street
        fom.DOB = dob
        fom.vechile_no = vechile_no
        fom.vechile_color = vechile_color
        fom.vechile_name = vechile_name
        fom.license_no = license_no
        fom.permanent_country = permanent_country
        fom.permanent_district = permanent_district
        fom.permanent_address = permanent_address
        fom.permanent_muncipalicity = permanent_muncipalicity
        fom.permanent_ward = permanent_ward
        fom.permanent_tole = permanent_tole
        fom.save()    
        return HttpResponse('Sucessfully Signed Up ')
    else:
        return render(request, 'admin/adddeliveryboy.html', {'form':form})
    return render(request, 'admin/adddeliveryboy.html', {'form':form})

def addwholeseller(request):
    form = WholeSellerForm(request.POST or None)
    if form.is_valid():
        foms = WholeSellerForm(request.POST)
        cd = form.cleaned_data
        fullname = cd['fullname']
        email = cd['email']
        password = cd['password']
        country = cd['country']
        district = cd['district']
        province = cd['province']
        ward_no = cd['ward_no']
        street = cd['street']
        company = cd['shopname']
        fom = foms.save(commit=False)
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '2')
        fom.admin = vend
        fom.fullname = fullname
        fom.country = country
        fom.district = district
        fom.province = province
        fom.ward_no = ward_no
        fom.street = street
        fom.shopname = company
        fom.save()    
        return HttpResponse('Sucessfully Signed Up ')
    else:
        return render(request, 'admin/addwholeseller.html', {'form':form})
    return render(request, 'admin/addwholeseller.html', {'form':form})


def kycrequest(request):
    verifyC = verifyrequest.objects.all()
    
    dist = {
        'vc': verifyC
    }
    return render(request, 'admin/verifyrequest.html', dist)

def verifyVendor(request, id):
    try:
        verifyuser = Vendor.objects.get(id= id)
        verifyuser.verified = True
        verifyuser.save()
        verifyA = verifyrequest.objects.filter(requester = verifyuser.admin.id)
        verifyA.delete()
        messages.success(request, 'Successfully Verified')
        return HttpResponseRedirect(reverse('owner:vendorreport', kwargs={'id':id}))
    except:
        messages.success(request, 'Something went wrong!')
        return HttpResponseRedirect(reverse('owner:vendorreport', kwargs={'id':id}))       
   
def verifySeller(request, id):
    try:
        verifyuser = Wholeseller.objects.get(id= id)
        verifyuser.verified = True
        verifyuser.save()
        verifyA = verifyrequest.objects.filter(requester = verifyuser.admin.id)
        verifyA.delete()
        messages.success(request, 'Successfully Verified')
        return HttpResponseRedirect(reverse('owner:wholesellerReport', kwargs={'id':id}))
    except:
        messages.success(request, 'Something went wrong!')
        return HttpResponseRedirect(reverse('owner:wholesellerReport', kwargs={'id':id}))
    
   