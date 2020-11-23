from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Vendor, CustomUser
from .forms import VendorForm, WholeSellerForm, AffiliateForm, CustomerForm
from .getLocation import send_loc
from django.contrib import messages

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
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
                return HttpResponseRedirect(reverse('staff:wholesellerdashboard'))
            if user.user_type == "3":
                return HttpResponseRedirect(reverse('staff:vendordashboard'))
            if user.user_type == "4":
                return HttpResponseRedirect(reverse('staff:deliverydashboard'))
            if user.user_type == "5":
                return HttpResponseRedirect(reverse('staff:affliliatedashboard'))
            if user.user_type == "6":
               return HttpResponseRedirect(reverse('staff:userdashboard'))
        else:
            messages.error(request, 'Incorrect Email or Password')
            return HttpResponseRedirect(reverse('shop:login'))
    else:
        return HttpResponse("<H2>You Are now not Login</H2>")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def enrollvendor(request):
    form = VendorForm(request.POST or None)
    g = send_loc(request)
    info = g.address.split(',')
    form.fields['district'].initial = info[0]
    form.fields['province'].initial = info[1]
    form.fields['country'].initial = info[2]
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
        
        messages.success(request, 'User Created Sucessfully. Please Login')
        return HttpResponseRedirect(reverse('shop:login'))
    else:
        return render(request, 'normal/enrollvendor.html', {'form':form})
    
    return render(request, 'normal/enrollvendor.html', {'form':form})

def enrollwholeseller(request):
    form = WholeSellerForm(request.POST or None)
    g = send_loc(request)
    info = g.address.split(',')
    form.fields['district'].initial = info[0]
    form.fields['province'].initial = info[1]
    form.fields['country'].initial = info[2]
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
        messages.success(request, 'User Created Sucessfully. Please Login')
        return HttpResponseRedirect(reverse('shop:login'))
    else:
        return render(request, 'normal/enrollwholeseller.html', {'form':form})
    return render(request, 'normal/enrollwholeseller.html', {'form':form})
        
     
def enrollaffiliate(request):
    form = AffiliateForm(request.POST or None)
    g = send_loc(request)
    info = g.address.split(',')
    form.fields['district'].initial = info[0]
    form.fields['province'].initial = info[1]
    form.fields['country'].initial = info[2]
    
    if form.is_valid():
        foms = AffiliateForm(request.POST)
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
        citizen = cd['citizen_number']
        dob = cd['DOB']
        permanentD = cd['permanent_district']
        permenetM = cd['permanent_muncipalicity']
        permanentA = cd['permanent_address']
        permamentW = cd['permanent_ward']

        fom = foms.save(commit=False)
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '5')
        fom.admin = vend
        fom.fullname = fullname
        fom.country = country
        fom.district = district
        fom.province = province
        fom.ward_no = ward_no
        fom.street = street
        fom.citizen_number = citizen
        fom.DOB = dob
        fom.permanent_district = permanentD
        fom.permanent_muncipalicity = permenetM
        fom.permanent_ward = permanentA
        fom.permanent_address = permamentW
        fom.gender = gender

        fom.save()    
        messages.success(request, 'User Created Sucessfully. Please Login')
        return HttpResponseRedirect(reverse('shop:login'))
    else:
        return render(request, 'normal/enrollaffilite.html', {'form':form})
    return render(request, 'normal/enrollaffilite.html', {'form':form})


def registerA(request):
    form = CustomerForm(request.POST or None)
    
    if form.is_valid():
        foms = CustomerForm(request.POST)
        cd = form.cleaned_data
        fullname = cd['fullname']
        email = cd['email']
        password = cd['password']
        
        fom = foms.save(commit=False)
        vend = CustomUser.objects.create_user(email = email, password = password, username = email, user_type = '6')
        fom.admin = vend
        fom.fullname = fullname
        fom.save()   
        
        
        messages.success(request, 'User Created Sucessfully. Please Login')
        return HttpResponseRedirect(reverse('shop:login'))
    else:
        return render(request, 'normal/enrolluser.html', {'form': form})
    return render(request, 'normal/enrolluser.html', {'form': form})



def loginpage(request):
    return render(request, 'normal/loginppage.html')


        