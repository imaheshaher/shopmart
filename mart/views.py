from django.shortcuts import render,redirect,get_object_or_404
from django.utils.decorators import method_decorator
from django.db.models import Q,Count
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.views.generic import View,ListView,UpdateView,CreateView,DetailView,FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .filter import *
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import ShopSerializer



def filterdata(request):
  distid=request.GET.get('district')
  
def design(request):
  
  form=DistrictForm()
  dist=District.objects.all()
  distdata=District.objects.all()
  
  context = {
    'dist':dist,
    'form':form,
    'distdata':distdata,
  
  }
  return render(request,'home1.html',context)
def load_cities(request):
  
  
  distid=request.GET.get('district')
  
  tels=Talukas.objects.filter(district_id=distid).order_by('district')
  
  context ={
      'tels':tels,
    }
  return render(request,'load_cities.html',context)
def index(request):
  '''shop_data=ShopDetail.objects.all()
  cityfilter=CityFilter(request.GET,queryset=shop_data)
  city=request.GET.get('city')
  query=request.GET.get('q')
  if not query:
    query=None
  if not city:
    city=None
  #if len(city)>0:
  #   #("city =",len(city))
  shopname=None
  context={'shopname':shopname}
  if query and city==None:
    shopname=shop_data.filter(Q(shop_name__icontains=query))
    context['shopname']=shopname
  elif query and city:
    shopname=shop_data.filter(Q(shop_name__icontains=query), city=int(city))
    context['shopname']=shopname
  elif query==None and city==None:
    context['shopname']=cityfilter.qs
  else:
    context['shopname']=cityfilter.qs
     #(city)
  context['cityfilter']=cityfilter
  context['queryset']=cityfilter.qs
  '''
  '''context = {
    'cityfilter':cityfilter,
    'queryset':cityfilter.qs,
    
    }
    '''
  dist=District.objects.all()
  tel=Talukas.objects.all()
  data=ShopDetail.objects.all()
  cityfilter=CityFilter(request.GET,queryset=data)
  context={
    'dist':dist,
    'tel':tel,
    'filter':cityfilter
  }
  #   #(context['shopname'])
  return render(request,'shopdata.html',context)
def home1(request):
  return render(request,'login_page.html')
  
  
def get_user(user):
  qs=Seller.objects.filter(user=user)
  if qs.exists():
    return qs[0]
  return None
  

def register(request):
  if request.method=='POST':
    form=UserForm(request.POST)
    form1=CustomerForm(request.POST)
    if form.is_valid() and form1.is_valid():
      userform=form.save(commit=False)
      uname=request.POST['username']
      password=request.POST['password']
      
      userform.set_password(password)
      userform.save()
      custform=form1.save(commit=False)
      custform.user=userform
      custform.mob_no=uname
      custform.save()
      return redirect('mart:home1')
  else:
    form=UserForm()
  
  return render(request,'c_register.html')

def s_register(request):
  if request.method=='POST':
    form=UserForm(request.POST)
    form1=SellerForm(request.POST)
    if form.is_valid() and form1.is_valid():
      userform=form.save(commit=False)
      uname=request.POST['username']
      password=request.POST['password']
      
      userform.set_password(password)
      userform.save()
      sellerform=form1.save(commit=False)
      sellerform.user=userform
      sellerform.mob_no=int(uname)
      sellerform.save()
      
      return redirect('mart:home1')
      
  else:
    form=UserForm()
  
  return render(request,'register_page.html')
def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    
    user=auth.authenticate(username=username,password=password)
    
    if user is not None:
      auth.login(request,user)
      if user.is_seller:
        
        try:
          s=Seller.objects.get(user_id=request.user.id)
          shop=ShopDetail.objects.get(user_id=s.id)
          return redirect('mart:profiledetail',shop.id)
        except:
          return redirect('mart:createshop',request.user)
          
      return redirect("mart:sellerdetail")
    else:
      return HttpResponse("Mobile Number or Password are incorrect <a href='home1'>login</a>")
      
  return render(request,'login_page.html')

def logout(request):
  auth.logout(request)
  return redirect("mart:sellerdetail")

def search(request):
  shop_data=ShopDetail.objects.all()
  shop_filter=ShopFilter(request.GET,queryset=shop_data)
  sfilter=None
  sfilter=request.GET.get('name')
  lst=['shop_name','category','address','city','pincode']
  context = {
    'filter':shop_filter,
    'sfilter':sfilter,
    'lst':lst
    
  }
  
  return render(request,'searchfilter.html',context)

class SearchView(View):
  def getdistrict(self,request,*args,**kwargs):
    distid=self.request.GET.get('district')
    
  def get(self,request,*args,**kwargs):
    shop_data=ShopDetail.objects.all()
    cityfilter=CityFilter(self.request.GET,queryset=shop_data)
    context={}
    context['cityfilter']=cityfilter
    context['queryset']=cityfilter.qs
    
      
    
    return render (request,'seller_list.html',context)

class SellerDetail(ListView):
  model=ShopDetail
  template_name = "seller_list.html"
  
  context_object_name='queryset'
  
  def get_context_data(self,**kwargs):
    data=ShopDetail.objects.all().order_by('-pk')
    
    cityfilter=CityFilter(self.request.GET,queryset=data)
    context=super().get_context_data(**kwargs)
    form=DistrictForm()
    context['cityfilter']=cityfilter
    context['queryset']=cityfilter.qs
    context['form']=form
    
    #   #(context)
    return context
  
def profile(request,id):

  seller=Seller.objects.filter(user_id=request.user.id)
  #shop=ShopDetail.objects.filter(user_id=seller.id)
  #   #(shop)
  context ={
    'seller':seller,
   # 'shop':shop
  }
  return render(request,'profile.html',context)
  
class ProfileDetail(DetailView):
  model=ShopDetail
  
  template_name='profile.html'
  
  def get_context_data(self,**kwargs):
    pk=self.kwargs['pk']
    
    context=super(ProfileDetail,self).get_context_data(**kwargs)
    context['shop']=ShopDetail.objects.filter(id=pk)
    context['seller_product']=Seller_Product.objects.filter(seller_id_id=pk)
    context['seller_service']=Seller_Service.objects.filter(seller_id_id=pk)
    context['service_form']=Seller_Service_Form()
    context['product_form']=Seller_Product_Form()
    return context

'''@login_required
def shop_update_data(request):
  if request.user.is_authenticated:
    s=Seller.objects.get(user_id=request.user.id)
    shop=ShopDetail.objects.get(user_id=s.id)
       #(shop)
    id=shop.id
    seller=get_object_or_404(ShopDetail,pk=id)
  form=ShopForm(request.POST or None,instance=seller)
  if form.is_valid():
    form.save()
    return HttpResponse('form updated')
  
  return render(request,'s_profileupdate.html',{'form':form})  
'''
class shopupdate(UpdateView):
  model=ShopDetail
  form_class=ShopForm
  template_name='s_profileupdate.html'
  
  
  '''
  def get_context_data(self,**kwargs):
    
    
    context=super().get_context_data(**kwargs)
    
    return context
    '''
  
  def get_object(self,*args,**kwargs):
    
    id_=get_object_or_404(Seller,pk=self.kwargs['pk'])
    id=id_.id
    
    
    if self.request.user.id!=id_.user_id:
      
      id_=Seller.objects.get(user_id=self.request.user.id)
      id=id_.id
    return get_object_or_404(ShopDetail,user_id=id)
  '''  
  def form_valid(self,form):
    return super().form_valid(form)
    '''
    
    

class createshop(CreateView):
  
  model=ShopDetail
  form_class=ShopForm
  
  template_name='s_profileupdate.html'
  success_url="/sellerdetail"

  def get_shop(self,**kwargs):
    print('data get')
  def get_context_data(self,**kwargs):
    
    context = super().get_context_data(**kwargs)
    
    return context
    
  def form_valid(self,form):
    form.instance.user=get_user(self.request.user)
    selid=Seller.objects.get(user_id=self.request.user.id)
    try:
      shop=ShopDetail.objects.get(user_id=selid.id)
      return redirect("mart:shopupdate",selid.id)
    except:
      
      form.save()
    return redirect("mart:profiledetail",form.instance.pk)
    '''
  def form_valid(self,form):
    s=Seller.objects.filter(user=self.request.user)[0]
       #(s)
    form.instance.user=s.user
    return super(createshop,self).form_valid(form)
  '''
def CreateShopdetail(request,id):
  s=Seller.objects.get(user=request.user)
  
  if request.method=='POST':
    form=ShopForm(request.POST,request.FILES)
    if form.is_valid():
      shop=form.save(commit=False)
      
      
      
      shop.user=s
      shop.save()
      return redirect('mart:profile',request.user)
  else:
    form=ShopForm()
    
  return render(request,'s_profileupdate.html',{'form':form})
  
  
  
def all_shop(request):
  shop=ShopDetail.objects.all()
  form=CityFilter(request.GET,queryset=shop)
  
  
  context={
    
    'form':form,
    'shop':form.qs,
    
    
  }
  return render(request,'all_shop.html',context)
  

class All_shop(ListView):
  model=ShopDetail
  template_name = "all_shop.html"
  context_object_name='shop'
  def get_context_data(self,**kwargs):
    data=ShopDetail.objects.all()
    district=District.objects.all()
    context['district']=district
    context=super().get_context_data(**kwargs)
    #   #(context)
    return context
    
@login_required
def updateform(request):
  sid=get_object_or_404(Seller,user_id=request.user.id)
  obj=get_object_or_404(ShopDetail,user_id=sid.id)
  
  id=obj.id
  shop=ShopDetail.objects.get(id=id)
  if shop.status:
    shop.status=False
  else:
    shop.status=True
  shop.save()
  
  return redirect('mart:profiledetail',pk=id)
  
  
#APIView

class ShopListAPI(APIView):
  def get(self,request):
    shopdetail=Category.objects.all()
    serializer=ShopSerializer(shopdetail,many=True)
    return Response(serializer.data)
    
    
    
'''  
def add_data(request):
  for d in dict:
    name=d['district']
    District.objects.create(district=name)
    
'''

@login_required
def add_product(request):
  try:
    sid=Seller.objects.get(user_id=request.user.id)
  except:
    return HttpResponse("May be You not have any Shop or Service")
  form=Seller_Product_Form(request.POST,request.FILES)
  
  shopid=ShopDetail.objects.get(user_id=sid.id)
  
  if request.method=='POST':
    if form.is_valid():
      product_form=form.save(commit=False)
      product_form.seller_id=sid
      product_form.save()
      return redirect("mart:profiledetail",shopid.id)
    else:
      return HttpResponse("fill proper info")
    
  else:
    form=Seller_Product_Form()
    
  return redirect("mart:profiledetail",shopid.id)
  

@login_required
def add_service(request):
  try:
    sid=Seller.objects.get(user_id=request.user.id)
  except:
    return HttpResponse("May be You not have any Shop or Service")
  form=Seller_Service_Form(request.POST,request.FILES)
  
  shopid=ShopDetail.objects.get(user_id=sid.id)
  
  if request.method=='POST':
    if form.is_valid():
      service_form=form.save(commit=False)
      service_form.seller_id=sid
      service_form.save()
      return redirect("mart:profiledetail",shopid.id)
    else:
      return HttpResponse("fill proper info")
    
  else:
    form=Seller_Service_Form()
    
  return redirect("mart:profiledetail",shopid.id)