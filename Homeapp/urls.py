from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('home/', views.home, name ='home'),
    path('account/', views.account, name ='account'),
    path('deals/', views.deals, name ='deals'),
    path('help/', views.help, name ='help'),
    path('registry/', views.registry, name ='registry'),
    path('sell/', views.sell, name ='sell'),
]