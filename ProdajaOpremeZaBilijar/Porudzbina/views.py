from django.shortcuts import render

from KorpaZaKupovinu.korpa import Korpa
from .models import OrderItem
from .forms import OrderForm

# Create your views here.

def AddOrder(request):
    cart = Korpa(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                print('cart', item)
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.DeleteCartFromSession()
            return render(request, 'Porudzbina/created.html', { 'order': order })
        
    else: 
        form = OrderForm()
    
    return render(request, 'Porudzbina/create.html', { 'cart': cart, 'form': form })
   


