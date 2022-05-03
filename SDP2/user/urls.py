from django.urls import path
from . import views
urlpatterns=[
   path('reg/',views.userregistration,name='reg'),
   path('login/',views.loginpage,name='login'),
   path('',views.home,name='home'),
   path('about/', views.about, name="about"),
   path('contact/', views.contact, name="contact"),
   path('product/', views.products, name="products"),
   path('footware/',views.footware,name='footware'),
   path('clothing/',views.clothing,name='clothing'),
   path('fitnessandsports',views.fitnessandsports,name='fitnessandsports'),
   path('homedecor/',views.homedecor,name='homedecor'),
   path('electronics/',views.electronics,name='electronics'),
   path('groceriesandfood/',views.groceriesandfood,name='groceriesandfood'),
   path('cart/',views.cart,name='cart'),
   path('checkout/',views.checkout,name='checkout'),
   path('order/',views.order,name='order'),
   path('phnpe/',views.phnpe,name='phnpe'),
   path('gpay/',views.gpay,name='gpay'),
   path('index1/',views.index1,name='index1'),



]