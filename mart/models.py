from PIL import Image
from django.db import models
from django.contrib.auth.models import  AbstractUser,User
from django.contrib.auth import get_user_model
from shopmart import settings
from django.shortcuts import reverse
# Create your models here.
class User(AbstractUser):
  @property
  def is_seller(self):
    if hasattr(self,'seller'):
      return True
      
    return False
class Customer(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  mob_no=models.IntegerField()
  city=models.CharField(max_length=100)
  pincode=models.IntegerField()
  address=models.CharField(max_length=100)
  
  def __str__(self):
    return str(self.user)
    
class Seller(models.Model):
  user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  mob_no=models.IntegerField()
  shop_name=models.CharField(max_length=20,blank=True)
  city=models.CharField(max_length=100,blank=True)
  
  address=models.CharField(max_length=100,blank=True)
  slug=models.SlugField(blank=True)
  def __str__(self):
    return str(self.user)
    
  def get_absolute_url(self):
    return reverse("mart:profiledetail",kwargs = {
      'slug':self.user
    })
    
  def get_mobile_no(self):
    return self.mob_no
    '''
CHOICES = (
  
  ('dals and pulses','Dals and Pulses'),
  ('Edible Oil','Edible Oil')
  )
class Product(models.Model):
  Category=models.CharField(max_length=20,choices=CHOICES,default='dals and Pulses')
  
    '''

class City(models.Model):
  city=models.CharField(max_length=30)
  
  
  def __str__(self):
    return str(self.city)
  def get_city(self):
    
    return str(self.city)
class Category(models.Model):
  category=models.CharField(max_length=50)
  
  def __str__(self):
    return str(self.category)
    

class District(models.Model):
  district=models.CharField(max_length=40)
  
  def __str__(self):
    return str(self.district)

class Talukas(models.Model):
  district=models.ForeignKey(District,on_delete=models.CASCADE)
  taluka=models.CharField(max_length=40)
  
  def __str__(self):
    return str(self.taluka)

class ShopDetail(models.Model):
  user=models.ForeignKey(Seller,on_delete=models.CASCADE)
  shop_name=models.CharField(max_length=200)
  image=models.ImageField()
  
  shop_name=models.CharField(max_length=20)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
  district=models.ForeignKey(District,on_delete=models.CASCADE)
  city=models.ForeignKey(Talukas,on_delete=models.CASCADE,blank= True)
  pincode=models.IntegerField()
  address=models.CharField(max_length=100)
  
  status=models.BooleanField(default=True)
  working_time=models.CharField(max_length=50)
  todays_special=models.CharField(max_length=150)
  description=models.TextField()
  
  def save(self):
    super().save()
    image=Image.open(self.image.path)
    if image.height!=150 or image.width!=120:
      new_img=(150,120)
      image.resize(new_img)
      image.save(self.image.path)
  
  def __str__(self):
    return str(self.shop_name)

  def get_absolute_url(self):
    return reverse("mart:profiledetail", kwargs = {
      "pk":self.pk
    })
  def get_update_url(self):
    return reverse("mart:shopupdate", kwargs = {
      "pk":self.pk
    })
    
class Address(models.Model):
  district=models.ForeignKey(District,on_delete=models.CASCADE)
  taluka=models.ForeignKey(Talukas,on_delete=models.CASCADE)
  
  
class Seller_Product(models.Model):
  seller_id=models.ForeignKey(Seller,on_delete=models.CASCADE)
  product_image=models.ImageField()
  product_name=models.CharField(max_length=50,blank=True)
  product_price=models.IntegerField(blank=True)
  product_brand=models.CharField(max_length=50,blank=True)


  def __str__(self):
    return str(self.seller_id)
    
  def get_product_url(self):
    return self.pk

  
class Seller_Service(models.Model):
  
  seller_id=models.ForeignKey(Seller,on_delete=models.CASCADE)
  service_image=models.ImageField(blank=True)
  service_name=models.CharField(max_length=50,blank=True)
  service_describe=models.CharField(max_length=100,blank=True)
  
  def __str__(self):
    return str(self.seller_id)
    
  def get_service_url(self):
    return self.pk
    
