
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'), 
    path('gallery',views.gall,name='gall'),
    path('reserv',views.reser,name='reser'),
    path('contact',views.contact,name='contact'),
    path('About',views.About,name='About'),
    path('Contactdata',views.contactdata,name='contactdata'),
    path('reservdata',views.reservation_data,name='reservationdata'),
    path('signup',views.sign,name='sign'),
    path('signupdata',views.signupdata,name='signupdata'),
    path('loggedin',views.login,name='login'),
    path('logindata',views.logindata,name='logindata'),
    path('room',views.room,name='room')
]
