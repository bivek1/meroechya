from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from shop.forms import VendorForm
from shop.models import CustomUser, Vendor
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required 
def homepage(request):
    return render(request, 'admin/dashboard.html')

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
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '3')
        fom = foms.save(commit=False)
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

def vendorreport(request , id):
    selected = get_object_or_404(Vendor, id = id)
    return render(request, 'admin/vendorreport.html', {'one': selected})
    