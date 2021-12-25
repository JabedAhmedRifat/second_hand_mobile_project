"""second_hand_mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from selling import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about , name='about'),
    path('sign_up/',views.sign_up , name='sign_up'),
    path('apple/',views.apple , name='apple'),
    path('mobile_brand/',views.mobile_brand , name='mobile_brand'),
    path('get_paid/',views.get_paid , name='get_paid'),
    path('evaluation/',views.evaluation , name='evaluation'),
    path('customer/',views.customer , name='customer'),
    path('google/',views.google , name='google'),
    path('mobile_no/',views.mobile_no , name='mobile_no'),
    path('motorola/',views.motorola , name='motorola'),
    path('nokia/',views.nokia , name='nokia'),
    path('oneplus/',views.oneplus , name='oneplus'),
    path('realme/',views.realme , name='realme'),
    path('samsung/',views.samsung , name='samsung'),
    path('vivo/',views.vivo , name='vivo'),
    path('xioami/',views.xioami , name='xioami'),
    
    
]


urlpatterns += staticfiles_urlpatterns()
