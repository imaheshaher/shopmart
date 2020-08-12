from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *
from django.contrib.auth import get_user_model

User=get_user_model()

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name','last_name','username','password']
    
class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    exclude = ['user']
    fields = ['city','pincode','address']
    
class SellerForm(forms.ModelForm):
  class Meta:
    model = Seller
    exclude = ['user']
    fields =[]
    
class ShopForm(forms.ModelForm):
  
  class Meta:
    model = ShopDetail
    exclude=['user',]
    fields = ['shop_name','image','category','district','city','address','pincode','status','working_time','todays_special','description']
    
    def __init__(self,*args,**kwargs):
      
      super().__init__(*args,**kwargs)
      
      self.fields['city'].queryset=Talukas.objects.none()
      
     
     
      if 'district' in self.data:
        
        try:
          district_id=int(self.data.get('district'))
          
          self.fields['city'].queryset=Talukas.objects.filter(district_id=district_id)
        except (ValueError,TypeError):
          pass
        
      elif self.instance.pk:
        self.fields['city'].queryset=self.instance.district.taluka_set.order_by('taluka')
        
      
class DistrictForm(forms.ModelForm):
  class Meta:
    model = Address
    fields=['district','taluka']
'''
  def __init__(self,*args,**kwargs):
    
    super().__init__(*args,**kwargs)
    
    self.fields['taluka'].queryset=Talukas.objects.none()
    
   
   
    if 'district' in self.data:
      print("dist" ,self.data)
      try:
        district_id=int(self.data.get('district'))
        print("distct id")
        self.fields['taluka'].queryset=Talukas.objects.filter(district_id=district_id)
      except (ValueError,TypeError):
        pass
      
    elif self.instance.pk:
      self.fields['taluka'].queryset=self.instance.district.taluka_set.order_by('taluka')
      
      '''
      
      
  
class Seller_Product_Form(forms.ModelForm):
  class Meta:
    model=Seller_Product
    exclude=['seller_id']
    fields=['product_image','product_name','product_price','product_brand']
    
    

class Seller_Service_Form(forms.ModelForm):
  class Meta:
    model=Seller_Service
    exclude=['seller_id']
    fields=['service_image','service_name','service_describe']
    
    