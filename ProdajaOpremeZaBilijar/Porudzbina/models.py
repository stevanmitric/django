from django.db import models
from ProdavnicaBilijara.models import Product

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self): return f'Order {self.id}'

    def GetTotalPriceOrder(self):
        return sum(item.GetTotalPrice() for item in self.items_order_o.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items_order_o', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items_order_p', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
