from django.urls import path
from . import views

app_name = 'prodavnicabilijara'
urlpatterns = [
    path('', views.ListaProizvoda, name='ListaProizvoda'),
    path('<slug:category_slug>/', views.ListaProizvoda, name='ListaProizvodaPoKategoriji'),
    path('<int:id>/<slug:slug>/', views.DetaljiProizvoda, name='DetaljiProizvoda')
]