from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from KorpaZaKupovinu.forms import FormaZaDodavanjeProizvodaUKorpu

from KorpaZaKupovinu.korpa import Korpa

def ListaProizvoda(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    cart = Korpa(request)

    return render(request, 'ProdavnicaBilijara/list.html',
                  { 'category': category, 'categories': categories,
                   'products': products, 'cart': cart })

def DetaljiProizvoda(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    cart = Korpa(request)
    formazadodavanjeproizvodaukorpu = FormaZaDodavanjeProizvodaUKorpu()

    return render(request, 'ProdavnicaBilijara/detail.html',
                  { 'product': product, 'formazadodavanjeproizvodaukorpu': formazadodavanjeproizvodaukorpu, 'cart': cart })
 
# Create your views here.
