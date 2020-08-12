from .models import *
def user_profile(request):
  queryset=None
  if request.user.is_authenticated:
    if request.user.is_seller:
      sid=request.user.id
      
      selid=Seller.objects.filter(user=sid)[0]
      
      queryset=ShopDetail.objects.filter(user=selid.id)
      #print(queryset.id)
  context = {
  'shop':queryset
  }
  return context
  