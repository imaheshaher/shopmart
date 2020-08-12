from .models import  *
from .models import City
import django_filters

ob=City()
class ShopFilter(django_filters.FilterSet):
  class Meta:
    model=ShopDetail
    fields=['shop_name','category','city','address','pincode','description']

class CityFilter(django_filters.FilterSet):
  
  class Meta:
    model=ShopDetail
    fields ={
      'district':['exact',],
      'city':['exact'],
      'category':['exact'],
      'shop_name':['icontains',]
    }
    
  