from django import forms
from .models import Vendor, Wholeseller, Customer, Affiliate, CustomUser
from django.core.exceptions import ValidationError
class VendorForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', max_length = 200, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    re_password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}))
    class Meta:
       model = Vendor 
       fields = ('fullname', 'email', 'password','re_password','country', 'district', 'province', 'ward_no', 'street', 'companyname')
       labels = {
           'fullname':'Full Name',
           'country' : 'Country',
           'district': 'District',
           'province': 'Province',
           'ward_no' : 'Ward No',
           'street' : 'Street',
           'companyname': 'Company Name',
           'vat'    : 'Vat No. of Company',
           'profile_pic' :'User Profile',
           'KYC'         : 'Scan copy of National Id',
           'taxpic'     : 'Tax Clear copy',
           'number' :'Phone Number'
           
       }
       widgets = {
           'fullname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Full Name'}),
           'country': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
           'district': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
           'province': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Province State'}),
           'ward_no': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Ward'}),
           'street': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Street Address'}),
           'companyname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Your Company Name'}),
            'vat': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Company Vat Number'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Profile Pic of vendor'}),
            'KYC': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Company Name'}),
            'taxpic': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Company Name'}),
            'number': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Phone Number'}),
   }
       
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
    def clean_number(self):
        data = self.cleaned_data['number']
        d = str(data)
        if len(d) > 10 or len(d) < 10 :
            raise ValidationError("Number can not be less or more than 10 digits")
        if not d.startswith('98'):
            raise ValidationError("Nepali number should start with 98")
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        d = str(data)
        if len(d) < 6:
            raise ValidationError("Password must be greater than 6 digits")
        return data
    def clean_re_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('re_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password Did not Match')
        return password2
       
class WholeSellerForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', max_length = 200, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    re_password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}))
    class Meta:
        model = Wholeseller
        fields = ('fullname', 'email', 'password','re_password','country', 'district', 'province', 'ward_no', 'street', 'shopname')
        labels ={
            'fullname':'Full Name',
           'country' : 'Country',
           'district': 'District',
           'province': 'Province',
           'ward_no' : 'Ward No',
           'street' : 'Street',
           'shopname': 'Shop Name',
           'vat'    : 'Vat No. of Shop',
           'profile_pic' :'User Profile',
           'KYC'         : 'Scan copy of National Id',
           'taxpic'     : 'Tax Clear copy',
           'number' :'Phone Number'
        }
        widgets = {
           'fullname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Full Name'}),
           'country': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Country'}),
           'district': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
           'province': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Province State'}),
           'ward_no': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Ward'}),
           'street': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Street Address'}),
           'shopname': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Your Shop Name'}),
            'vat': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Company Vat Number'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Profile Pic of vendor'}),
            'KYC': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Company Name'}),
            'taxpic': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Company Name'}),
            'number': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Your Phone Number'}),
   }
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
    def clean_number(self):
        data = self.cleaned_data['number']
        d = str(data)
        if len(d) > 10 or len(d) < 10 :
            raise ValidationError("Number can not be less or more than 10 digits")
        if not d.startswith('98'):
            raise ValidationError("Nepali number should start with 98")
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        d = str(data)
        if len(d) < 6:
            raise ValidationError("Password must be greater than 6 digits")
        return data
    def clean_re_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('re_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password Did not Match')
        return password2