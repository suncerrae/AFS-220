# pages/urls.py
from django.urls import path
from . import views
from .views import AboutPageView,  CateringPageView, EditMenuPageView


# MenuPageView,

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu, name='menu'), 
    path('editmenu/', EditMenuPageView.as_view(), name='editmenu'),
    path('catering/', CateringPageView.as_view(), name='catering'), 
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order, name='order'),
    path('cart/', views.getcart, name='cart'),
    path('cateringOrder/', views.cateringOrder, name='cateringOrder'),
    path('sides/', views.saveSide, name='sides'),

]