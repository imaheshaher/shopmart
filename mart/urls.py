from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import re_path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
app_name='mart'
urlpatterns = [
    
    path('filterdata',views.filterdata,name='filterdata'),
    path('design',views.design,name='design'),
    path('index',views.index,name='index'),
    path('',views.SellerDetail.as_view(),name='sellerdetail'),
    path('load/cities',views.load_cities,name='ajax_load_cities'),
    path('home1',views.home1,name='home1'),
    #path('refresh1',views.refresh1,name='refresh'),
    path('register',views.register,name='register'),
    path('s_register',views.s_register,name='s_register'),
    path('login',views.login,name='login'),
    path('sellerdetail',views.SellerDetail.as_view(),name='sellerdetail'),
    path('profile/<slug:id>/',views.profile,name='profile'),
    path('shopupdate/<pk>',login_required(views.shopupdate.as_view()),name='shopupdate'),
    #path('shop_update_data',views.shop_update_data,name='shop_update_data'),
    path('createshop/<slug:id>',views.createshop.as_view(),name='createshop'),
    path('createshopdetail/<slug:id>',views.CreateShopdetail,name='createshopdetail'),
    path('logout',views.logout,name='logout'),
    path('profiledetail/<pk>/',views.ProfileDetail.as_view(),name='profiledetail'),
    path('search',views.SearchView.as_view(),name='search'),
    url(r'^searchfilter/$',views.search,name='searchfilter'),
    path('all_shop',views.all_shop,name='all_shop'),
    path('updateform',views.updateform,name='updateform'),
    
    #path('all_shop',views.All_shop.as_view(),name='all_shop')
  
    # rest api url 
    path('shop-list-api',views.ShopListAPI.as_view(),name="shop-list-api"),
    # add seller product
    re_path(r'profiledetail/\d+/add-product',views.add_product,name='add-product'),
    #add service url
    re_path(r'profiledetail/\d+/add-service',views.add_service,name='add-service'),
    #update product
    path("product_update/<pk>",views.product_update,name='product_update'),
    #delete product_update
    path("product_delete/<pk>",views.delete_product,name='product_delete'),
    
    #update service
    path("service_update/<pk>",views.service_update,name='product_update'),
    #delete service
    path("service_delete/<pk>",views.delete_service,name='product_delete'),
  ]
  
  

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)                   