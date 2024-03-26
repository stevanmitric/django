from django.urls import path
from . import views

app_name= 'Order'
urlpatterns = [
    path('kreirajporudzbinu/', views.AddOrder, name='AddOrder'),
]