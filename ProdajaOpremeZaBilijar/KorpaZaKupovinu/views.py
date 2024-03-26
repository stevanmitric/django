from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaBilijara.models import Product
from .korpa import Korpa
from .forms import FormaZaDodavanjeProizvodaUKorpu

# Create your views here.

@require_POST
def AddToCart(request, product_id):
    cart = Korpa(request)
    product = get_object_or_404(Product, id=product_id)
    form = FormaZaDodavanjeProizvodaUKorpu(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.Add(product=product, quantity=cleaned_data['quantity'], add_to_quantity=cleaned_data['add_to_quantity'])
    
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

@require_POST
def RemoveFromCart(request, product_id):
    print('product', product_id)
    cart = Korpa(request)
    product = get_object_or_404(Product, id=product_id)
    
    cart.Remove(product)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')

def DetaljiKorpe(request):
    cart = Korpa(request)
    for item in cart: 
        print('item', item)
        item['formazaazuriranjekolicine'] = FormaZaDodavanjeProizvodaUKorpu(
            initial={ 'quantity': 1, 'add_to_quantity': True }
        )
    return render(request, 'KorpaZaKupovinu/detail.html', { 'cart': cart })


