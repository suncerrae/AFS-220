# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Menu_Item , Service, ContactData, Carts, Side
# Create your views here.

from django import forms
from django.http import HttpResponseRedirect
from django.db import connection


class CateringPageView(TemplateView):
    template_name = 'catering.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class EditMenuPageView(TemplateView):
    template_name = 'editmenu.html'

def home(request):

    service = Service.objects.all()
    return render(request, "home.html", {'service':service} )

def menu(request):
    menu = Menu_Item.objects.all()
    side = Side.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = "20.00"

        menu_data = Menu_Item(name=name, description=description,price=price)

        menu_data.save()   
        
        
        return render(request, "editmenu.html")
        
    else:
         return render(request, "menu.html", {'menu': menu , 'side': side})

    return render(request, "menu.html", {'menu': menu, 'side': side} )

def contact(request):
     submitted = False
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = ContactData(name=name, email=email,subject=subject,message=message)

        contact_data.save()

        return render(request, 
         'contact.html', {'submitted': True})

        
     else:
         return render(request, 
         'contact.html', {'submitted': False})
    
     return render(request, 
         'contact.html'
       )

def order(request):
    submitted = False
    menu = Menu_Item.objects.all()
    side = Side.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        meat = request.POST.get('meat')
        side1 = request.POST.get('side1')
        side2 = request.POST.get('side2')
        price = request.POST.get('price')

        order_data = Carts(name=name,meat=meat, side1=side1, side2=side2,price=price)

        order_data.save()
        return render(request, 
         'order.html', {'submitted': True , 'menu': menu , 'side': side})

        
    else:
        return render(request, 
         'order.html', {'submitted': False , 'menu': menu , 'side': side})
 
    return render(request, 
         'contact.html', {'menu': menu , 'side': side} )

def getcart(request):
    if request.method == 'POST':
        name = request.POST.get('name')        
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, meat, side1, side2, price FROM pages_carts WHERE name = %s", [name])
            data = cursor.fetchone() 
            
        if data is not None:
            price = int(data[4]) * 20
            return render(request, 'cart.html', {'name': data[0], 'meat': data[1], 'side1': data[2], 'side2': data[3], 'count': data[4], 'show': True, 'price': price})
        else:
            return render(request, 'cart.html', { 'nodata': True})

    return render(request, 'cart.html')

def cateringOrder(request):
    submitted = False
    menu = Menu_Item.objects.all()
    side = Side.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        meat = request.POST.get('meat')
        side1 = request.POST.get('side1')
        side2 = request.POST.get('side2')
        price = request.POST.get('price')

        order_data = Carts(name=name,meat=meat, side1=side1, side2=side2,price=price)

        order_data.save()

        return render(request, 
         'cateringOrder.html', {'submitted': True, 'menu':menu , 'side': side})

        
    else:
        return render(request, 
         'cateringOrder.html', {'submitted': False, 'menu': menu , 'side': side})
         
    return render(request, 
         'cateringOrder.html', {'submitted': False , 'menu': menu, 'side': side}
       )

def saveSide(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        sides = Side(name=name)
        sides.save()   
        
        
        return render(request, "editmenu.html")
        
    else:
         return render(request, "editmenu.html")

    return render(request, "editmenu.html" )