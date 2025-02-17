from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self): return self.name
    def ApsolutniURL(self): return reverse('ProdavnicaBilijara:ListaProizvodaPoKategoriji', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='proizvodi/%Y/%m/%D', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))
        verbose_name_plural = 'products'

    def __str__(self): return self.name
    def ApsolutniURL(self): return reverse('ProdavnicaBilijara:DetaljiProizvoda', args=[self.id, self.slug])
