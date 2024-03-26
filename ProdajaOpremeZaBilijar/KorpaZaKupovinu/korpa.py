from decimal import Decimal
from django.conf import settings
from ProdavnicaBilijara.models import Product

class Korpa(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.ORDER_CART_SESSION_KEY)
        
        if not cart:
            cart = self.session[settings.ORDER_CART_SESSION_KEY] = {}

        # Ensure each item in the cart has the 'quantity' key
        for item in cart.values():
            item.setdefault('quantity', 0)

        self.cart = cart
    
    def __iter__(self): # for views and htmls
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cartcopy = self.cart.copy()

        for product in products:
            cartcopy[str(product.id)]['product'] = product
        for item in cartcopy.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item # returns generator
        
    def __len__(self): # for total number of products in cart
        return sum(item['quantity'] for item in self.cart.values())
    
    def Add(self, product, quantity=1, add_to_quantity=True):
        product_id = str(product.id)
        print('test', product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if add_to_quantity:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id]['quantity'] = quantity
        self.session.modified = True
    
    def Remove(self, product):
        print('PRO', product)
        if hasattr(product, 'id'):
            product_id = str(product.id)
            print('product id', product.id)
            if product_id in self.cart:
                del self.cart[product_id]
                self.session.modified = True

    def DeleteCartFromSession(self):
        del self.session[settings.ORDER_CART_SESSION_KEY]
        self.session.modified = True

    def GetTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
