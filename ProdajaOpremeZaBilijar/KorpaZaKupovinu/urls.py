from django.urls import path
from . import views

app_name = 'KorpaZaKupovinu'

urlpatterns = [
    path('', views.DetaljiKorpe, name='DetaljiKorpe'),
    path('add/<int:product_id>/', views.AddToCart, name='AddToCart'),
    path('remove/<int:product_id>/', views.RemoveFromCart, name='RemoveFromCart')
]