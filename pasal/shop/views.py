from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Vendor, CustomUser
from .forms import VendorForm, WholeSellerForm

# Create your views here.
def homepage(request):
    return render(request, 'base.html')


def dologin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username =  username, password = password)
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('owner:homepage'))
            if user.user_type == "2":
                return render(request, 'wholeseller/sellerboard.html')
            if user.user_type == "3":
                return render(request, 'vendor/vendorboard.html')
    else:
        return HttpResponse("<H2>You Are now not Login</H2>")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def enrollvendor(request):
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
        return HttpResponse('Sucessfully Sign Up ')
    else:
        return render(request, 'normal/enrollvendor.html', {'form':form})
    
    return render(request, 'normal/enrollvendor.html', {'form':form})

def enrollwholeseller(request):
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
        return render(request, 'normal/enrollwholeseller.html', {'form':form})
    return render(request, 'normal/enrollwholeseller.html', {'form':form})
        