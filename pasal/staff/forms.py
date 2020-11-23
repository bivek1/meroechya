from django import forms
from .models import Category, Sub_Category, Product, Brand
from django.core.exceptions import ValidationError

class AddCat(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'image')
        labels = {
            'name' : 'Category Name',
            'image': 'Choose a custom image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
        }
    def clean_name(self):
        data = self.cleaned_data['name']
        try:
            check = data.lower()
            same = Category.objects.get(name = check)
        except:
            return data
        raise ValidationError('This Category is added already')
    

class AddSubCat(forms.ModelForm):
    
    class Meta:
        model = Sub_Category
        fields = ('sub_name', 'category', 'image')
        widgets = {
            'sub_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sub Category Name'}),
            'category': forms.Select(attrs={'class':'form-control', 'placeholder':'Category Name'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
        }
    
   
class AddBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name', )
        widgets = {
            'brand_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Brand Name'}),
        }
    def clean_brand_name(self):
        data = self.cleaned_data['brand_name']
        try:
            check = data.lower()
            same = Brand.objects.get(brand_name = check)
        except:
            return data
        raise ValidationError('This Brand is added already')